# (In Process) Installing Arch Linux with Full Disk, External Backup and Zram Encryption, GRUB, LVM, Systemd and Busybox-based Initramfs
WILL INCLUDES GUIDES TO:
* +LUKS encryption
* +ext4 filesystem
* +LVM under LUKS
* +UEFI mode
* +Busybox-based initramfs
* +Systemd-based initramfs
* -Decrypt of both devices at same time
* -Zram implementation


(+ means already included and - means coming soon)

If you're only interested in installing Linux and not setting up dual boot with Windows, feel free to skip the Windows-related sections.

# Prepare the System

Before we dive into the installation process, let's ensure that your system is ready:

- **Data Backup:** Make sure you've backed up all your important data. We're about to make significant changes, and it's always wise to have a safety net.
- **UEFI Mode:** In your system's BIOS settings, set the boot mode to UEFI.

# Prepare the USB Drive

- **Ventoy Installation:** Start by installing [Ventoy](https://github.com/ventoy/Ventoy) on your USB drive. Ventoy is a versatile tool that allows you to easily create a multi-boot USB drive.
- **Download Arch ISO:** Head to [Arch Linux's official website](https://www.archlinux.org/download/) and download the Arch ISO image. Copy it to your USB drive.

# Disk Partition Structure

Here is an example to give you a clear picture of what the final disk partition structure will look like. If you're not interested in installing Windows, you can simply ignore the green parts.

| CRYPTLV 1            | CRYPTLV 2            | CRYPTLV 3            | Boot Partition | EFI Parition|
|----------------------|----------------------|----------------------|----------------|-------------|
| /                    | [SWAP]               | /home                | /boot          | /efi        |
| /dev/mapper/vg0-root | /dev/mapper/vg0-swap | /dev/mapper/vg0-home | /dev/sda2      | /dev/sda1   |

Please be aware that these names should be substituted with the actual device paths relevant to your system configuration:

| Device         | In this Doc          | Examples                      |
|----------------|----------------------|-------------------------------|
| Disk Device    | `/dev/<your-disk>`   | `/dev/sda`,  `/dev/nvme0n1`   |
| EFI Partition  | `/dev/<efi-disk>`    | `/dev/sda5`, `/dev/nvme0n1p1` |
| Boot Partition | `/dev/<boot-disk>`   | `/dev/sda6`, `/dev/nvme0n1p2` |
| LUKS Partition | `/dev/<luks-disk>`   | `/dev/sda7`, `/dev/nvme0n1p3` |

# Install Arch Linux

1.  Connect the USB drive and boot from the Arch Linux ISO.

1. Set your keyboard layout

        loakeys <keyboard-layout>

1. Set pacman configs, where "number" could be what you want, but not so higher

        vim /etc/pacman.conf

        # Uncomment and modifiy
        --> ParallelDownloads = <number>

1.  Make sure the system is booted in UEFI mode.
    The following command should display the directory contents without error.

        ls /sys/firmware/efi/efivars

1.  Connect to the internet.
    A wired connection is preferred since it's easier to connect.
    [More info](https://wiki.archlinux.org/index.php/Installation_guide#Connect_to_the_internet)

1.  Run `fdisk` and follow until step 11 to create Linux partitions.

        fdisk /dev/<your-disk>

1.  Create an empty GPT partition table using the `g` command.
    (**WARNING:** This will erase the entire disk.)

        Command (m for help): g
        Created a new GPT disklabel (GUID: ...).

1.  Create the EFI partition (`/dev/<efi-disk>`):

        Command (m for help): n
        Partition number: <Press Enter>
        First sector: <Press Enter>
        Last sector, +/-sectors or +/-size{K,M,G,T,P}: +256M

        Command (m for help): t
        Partition type or alias (type L to list all): uefi

1.  Create the Boot partition (`/dev/<boot-disk>`):

        Command (m for help): n
        Partition number: <Press Enter>
        First sector: <Press Enter>
        Last sector, +/-sectors or +/-size{K,M,G,T,P}: +1GB

        Command (m for help): t
        Partition type or alias (type L to list all): linux

1.  Create the LUKS partition (`/dev/<luks-disk>`):

        Command (m for help): n
        Partition number: <Press Enter>
        First sector: <Press Enter>
        Last sector, +/-sectors or +/-size{K,M,G,T,P}: <Press Enter>

        Command (m for help): t
        Partition type or alias (type L to list all): linux

1.  Print the partition table using the `p` command and check that everything is OK:

        Command (m for help): p

1.  Write changes to the disk using the `w` command.
    (Make sure you know what you're doing before running this command).

        Command (m for help): w

1.  Format the EFI and Boot Partitions.

        mkfs.fat -F 32 /dev/<efi-disk>
        mkfs.ext4 /dev/<boot-disk>

1.  Set up the encrypted partition.
    You can choose any other name instead of `luksLvmRoot`.

        cryptsetup --use-urandom luksFormat /dev/<luks-disk>
        cryptsetup open /dev/<luks-disk> luksLvmRoot

1.  Create an LVM volume group.
    You can choose any other name instead of `vg0`.

        pvcreate /dev/mapper/luksLvmRoot
        vgcreate vg0 /dev/mapper/luksLvmRoot

1.  Create LVM partitions (logical volumes).

    (**Update:** I don't create swap volume on disk anymore.
    Instead, I create a [zram](https://wiki.archlinux.org/title/Zram) device as swap space
    after finishing the installation process.)

    We create logical volumes for swap, root (`/`), and home (`/home`).
    Leave 256MiB of free space in the volume group because the `e2scrub` command requires
    the LVM volume group to have at least 256MiB of unallocated space to dedicate
    to the snapshot. For an 1TB disk:

        lvcreate --size 10G vg0 --name swap
        lvcreate --size 100G vg0 --name root
        lvcreate -l +100%FREE vg0 --name home
        lvreduce --size -256M vg0/home

1.  Format logical volumes.

        mkswap /dev/mapper/vg0-swap
        mkfs.ext4 /dev/mapper/vg0-root
        mkfs.ext4 /dev/mapper/vg0-home

1.  Mount new filesystems.

        mount /dev/mapper/vg0-root /mnt
        mount --mkdir /dev/<efi-disk> /mnt/efi
        mount --mkdir /dev/<boot-disk> /mnt/boot
        mount --mkdir /dev/mapper/vg0-home /mnt/home
        swapon /dev/mapper/vg0-swap

1.  Install the base system.
    We also install some useful packages like `git`, `vim`, and `sudo`.

        pacstrap -K /mnt base base-devel linux linux-firmware openssh git vim sudo

1.  Generate `/etc/fstab`. This file can be used to define how disk partitions,
    various other block devices, or remote filesystems should be mounted into the
    filesystem.

        genfstab -U /mnt > /mnt/etc/fstab

        # Check with
        cat /mnt/etc/fstab

1.  Enter the new system.

        arch-chroot /mnt /bin/bash

1. Execute `step 3` operation

1.  Set TimeZone.

        # See available timezones:
        ls /usr/share/zoneinfo/
       
        # Set timezone (you may should use other):
        ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

1.  Run hwclock(8) to generate `/etc/adjtime`.

        hwclock --systohc

1.  Set Locale.

        vim /etc/locale.gen (uncomment en_US.UTF-8 UTF-8 or another)
        locale-gen
        echo LANG=en_US.UTF-8 > /etc/locale.conf

1.  Set hostname.

        echo YourHostName > /etc/hostname

1.  Create a user.

        useradd -m -G wheel --shell /bin/bash YourUserName
        passwd YourUserName
        visudo
        # ---> Uncomment "%wheel ALL=(ALL) ALL"

1. Make keyboard config persistent

        vim /etc/vconsole.conf

        --> KEYMAP=<keyboard-layout>

1. Install LVM package

        pacman -S lvm2

1.  Configure `mkinitcpio` with modules needed to create the initramfs image.
        
        # For busybox-based initramfs
        vim /etc/mkinitcpio.conf

        --> HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block encrypt lvm2 filesystems fsck)

        # For systemd-based initramfs
        vim /etc/mkinitcpio.conf

        --> HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block sd-encrypt lvm2 filesystems fsck)

1. Recreate the initramfs image:

        mkinitcpio -P

1.  Setup GRUB.

        pacman -S grub efibootmgr
        grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB

    In `/etc/default/grub` edit the line GRUB_CMDLINE_LINUX as follows.
    Don't forget to replace `/dev/<luks-disk>` with the appropriate path.

        # To busybox-based initramfs
        GRUB_CMDLINE_LINUX="cryptdevice=/dev/$luks-disk$:luksLvmRoot root=/dev/vg0/root"

        # To systemd-based initramfs
        GRUB_CMDLINE_LINUX="rd.luks.name=$luks-disk-UUID-code$=luksLvmRoot root=/dev/vg0/root"

    Now generate the main GRUB configuration file:

        grub-mkconfig -o /boot/grub/grub.cfg

1.  Install `networkmanager` package and enable `NetworkManager` service
    to ensure you have Internet connectivity after rebooting.

        pacman -S networkmanager
        systemctl enable NetworkManager

1.  Exit new system and unmount all filesystems.

        exit
        umount -R /mnt
        swapoff -a

1.  Arch is now installed 🎉. Reboot.

        reboot

1.  Open BIOS settings and set `GRUB` as first boot priority.
    Save and exit BIOS settings. After booting the system, you should see the GRUB menu.

1.  Reboot again and log in to Arch linux with your username and password.

1.  Check internet connectivity.

        ping google.com

1.  Reboot!

# Notes

## Backup LUKS Header

It is important to make a backup of LUKS header so that you can access your data in case of emergency
(if your LUKS header somehow gets damaged).

Create a backup file:

    sudo cryptsetup luksHeaderBackup /dev/<luks-disk> --header-backup-file luks-header-backup-$(date -I)

Store the backup file in a safe place, such as a USB drive.
If something bad happens, you can restore the backup header:

    sudo cryptsetup luksHeaderRestore /dev/<luks-disk> --header-backup-file /path/to/backup_header_file

# References

- https://gist.github.com/mattiaslundberg/8620837
- https://wiki.archlinux.org/index.php/Installation_guide
- https://wiki.archlinux.org/title/Dm-crypt/Encrypting_an_entire_system#LVM_on_LUKS
- https://wiki.archlinux.org/title/GRUB
- https://joshrosso.com/docs/2020/2020-2-16-arch-windows-install/

---

Take a look at original creator [dotfiles repo](https://github.com/mjnaderi/dotfiles).