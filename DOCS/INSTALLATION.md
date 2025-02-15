# (In Process) Installing Arch Linux with Full Disk, External Backup, Zram Encryption, GRUB, LVM, Systemd, and Busybox-based Initramfs

## Includes Guides To:
* **LUKS encryption** (included)
* **ext4 filesystem** (included)
* **btrfs filesystem** (included)
* **LVM under LUKS** (included)
* **UEFI mode** (included)
* **Busybox-based initramfs** (included)
* **Systemd-based initramfs** (included)
* **Decrypt both devices at the same time** (included)
* **Zram implementation** (included)
* **Zswap implementation** (included)

If you're only interested in installing Linux and not setting up dual boot with Windows, feel free to skip the Windows-related sections.

## Prepare the System

Before we dive into the installation process, let's ensure that your system is ready:

- **Data Backup:** Make sure you've backed up all your important data. We're about to make significant changes, and it's always wise to have a safety net.
- **UEFI Mode:** In your system's BIOS settings, set the boot mode to UEFI.

## Prepare the USB Drive

- **Ventoy Installation:** Start by installing [Ventoy](https://github.com/ventoy/Ventoy) on your USB drive. Ventoy is a versatile tool that allows you to easily create a multi-boot USB drive.
- **Download Arch ISO:** Head to [Arch Linux's official website](https://www.archlinux.org/download/) and download the Arch ISO image. Copy it to your USB drive.

## Disk Partition Structure

Here is an example to give you a clear picture of what the final disk partition structure will look like. If you're not interested in installing Windows, you can simply ignore the green parts.

| CRYPTLV 1            | CRYPTLV 2            | CRYPTLV 3            | Boot Partition | EFI Partition |
|----------------------|----------------------|----------------------|----------------|---------------|
| /                    | [SWAP]               | /home                | /boot          | /efi          |
| /dev/mapper/vg0-root | /dev/mapper/vg0-swap | /dev/mapper/vg0-home | /dev/sda2      | /dev/sda1     |

Please be aware that these names should be substituted with the actual device paths relevant to your system configuration:

| Device         | In this Doc          | Examples                      |
|----------------|----------------------|-------------------------------|
| Disk Device    | `/dev/<your-disk>`   | `/dev/sda`,  `/dev/nvme0n1`   |
| EFI Partition  | `/dev/<efi-disk>`    | `/dev/sda5`, `/dev/nvme0n1p1` |
| Boot Partition | `/dev/<boot-disk>`   | `/dev/sda6`, `/dev/nvme0n1p2` |
| LUKS Partition | `/dev/<luks-disk>`   | `/dev/sda7`, `/dev/nvme0n1p3` |

## Install Arch Linux

1. Connect the USB drive and boot from the Arch Linux ISO.
2. Set your keyboard layout:

        loadkeys <keyboard-layout>

3. Set pacman configs, where "number" could be what you want, but not too high:

        vim /etc/pacman.conf

        # Uncomment and modify
        ParallelDownloads = <number>

4. Make sure the system is booted in UEFI mode. The following command should display the directory contents without error:

        ls /sys/firmware/efi/efivars

5. Connect to the internet. A wired connection is preferred since it's easier to connect. [More info](https://wiki.archlinux.org/index.php/Installation_guide#Connect_to_the_internet)

6. Run `fdisk` and follow until step 11 to create Linux partitions:

        fdisk /dev/<your-disk>

7. Create an empty GPT partition table using the `g` command. (**WARNING:** This will erase the entire disk.)

        Command (m for help): g
        Created a new GPT disklabel (GUID: ...).

8. Create the EFI partition (`/dev/<efi-disk>`):

        Command (m for help): n
        Partition number: <Press Enter>
        First sector: <Press Enter>
        Last sector, +/-sectors or +/-size{K,M,G,T,P}: +256M

        Command (m for help): t
        Partition type or alias (type L to list all): uefi

9. Create the Boot partition (`/dev/<boot-disk>`):

        Command (m for help): n
        Partition number: <Press Enter>
        First sector: <Press Enter>
        Last sector, +/-sectors or +/-size{K,M,G,T,P}: +1GB

        Command (m for help): t
        Partition type or alias (type L to list all): linux

10. Create the LUKS partition (`/dev/<luks-disk>`):

        Command (m for help): n
        Partition number: <Press Enter>
        First sector: <Press Enter>
        Last sector, +/-sectors or +/-size{K,M,G,T,P}: <Press Enter>

        Command (m for help): t
        Partition type or alias (type L to list all): linux

11. Print the partition table using the `p` command and check that everything is OK:

        Command (m for help): p

12. Write changes to the disk using the `w` command. (Make sure you know what you're doing before running this command).

        Command (m for help): w

13. Format the EFI and Boot Partitions:

        mkfs.fat -F 32 /dev/<efi-disk>
        mkfs.ext4 /dev/<boot-disk>

14. Set up the encrypted partition. You can choose any other name instead of `luksLvmRoot`:

        cryptsetup --use-urandom luksFormat /dev/<luks-disk>
        cryptsetup open /dev/<luks-disk> luksLvmRoot

15. Create an LVM volume group. You can choose any other name instead of `vg0`:

        pvcreate /dev/mapper/luksLvmRoot
        vgcreate vg0 /dev/mapper/luksLvmRoot

16. Create LVM partitions (logical volumes). (**Update:** I don't create swap volume on disk anymore. Instead, I create a [zram](https://wiki.archlinux.org/title/Zram) device as swap space after finishing the installation process.) We create logical volumes for swap, root (`/`), and home (`/home`). Leave 256MiB of free space in the volume group because the `e2scrub` command requires the LVM volume group to have at least 256MiB of unallocated space to dedicate to the snapshot. For a 1TB disk:

        lvcreate --size 10G vg0 --name swap
        lvcreate --size 100G vg0 --name root
        lvcreate -l +100%FREE vg0 --name home
        lvreduce --size -256M vg0/home

17. Format logical volumes:

        mkswap /dev/mapper/vg0-swap
        mkfs.ext4 /dev/mapper/vg0-root
        mkfs.ext4 /dev/mapper/vg0-home

    **Alternative: Format logical volumes with btrfs:**

        mkfs.btrfs /dev/mapper/vg0-root
        mkfs.btrfs /dev/mapper/vg0-home

18. Mount new filesystems:

        mount /dev/mapper/vg0-root /mnt
        mount --mkdir /dev/<efi-disk> /mnt/efi
        mount --mkdir /dev/<boot-disk> /mnt/boot
        mount --mkdir /dev/mapper/vg0-home /mnt/home
        swapon /dev/mapper/vg0-swap

    **Alternative: Mount new filesystems with btrfs subvolumes:**

        mount -o subvol=@ /dev/mapper/vg0-root /mnt
        mount --mkdir -o subvol=@home /dev/mapper/vg0-home /mnt/home
        mount --mkdir /dev/<efi-disk> /mnt/efi
        mount --mkdir /dev/<boot-disk> /mnt/boot
        swapon /dev/mapper/vg0-swap

19. Install the base system. We also install some useful packages like `git`, `vim`, and `sudo`:

        pacstrap -K /mnt base base-devel linux linux-firmware openssh git vim sudo

20. Generate `/etc/fstab`. This file can be used to define how disk partitions, various other block devices, or remote filesystems should be mounted into the filesystem:

        genfstab -U /mnt > /mnt/etc/fstab

        # Check with
        cat /mnt/etc/fstab

21. Enter the new system:

        arch-chroot /mnt /bin/bash

22. Execute `step 3` operation.

23. Set TimeZone:

        # See available timezones:
        ls /usr/share/zoneinfo/
       
        # Set timezone (you may should use other):
        ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

24. Run hwclock(8) to generate `/etc/adjtime`:

        hwclock --systohc

25. Set Locale:

        vim /etc/locale.gen (uncomment en_US.UTF-8 UTF-8 or another)
        locale-gen
        echo LANG=en_US.UTF-8 > /etc/locale.conf

26. Set hostname:

        echo YourHostName > /etc/hostname

27. Create a user:

        useradd -m -G wheel --shell /bin/bash YourUserName
        passwd YourUserName
        visudo
        # ---> Uncomment "%wheel ALL=(ALL) ALL"

28. Make keyboard config persistent:

        vim /etc/vconsole.conf

        --> KEYMAP=<keyboard-layout>

29. Install LVM package and some UI:

        pacman -S lvm2 plymouth

30. Configure `mkinitcpio` with modules needed to create the initramfs image:
        
        # For busybox-based initramfs
        vim /etc/mkinitcpio.conf

        --> HOOKS=(base udev autodetect microcode modconf kms plymouth keyboard keymap consolefont block encrypt lvm2 filesystems fsck)

        # For systemd-based initramfs
        vim /etc/mkinitcpio.conf

        --> HOOKS=(base systemd autodetect microcode modconf kms plymouth keyboard sd-vconsole block sd-encrypt lvm2 filesystems fsck)

31. Recreate the initramfs image:

        mkinitcpio -P

32. Setup GRUB:

        pacman -S grub efibootmgr
        grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB

    In `/etc/default/grub` edit the line GRUB_CMDLINE_LINUX as follows. Don't forget to replace `/dev/<luks-disk>` with the appropriate path:

        # To busybox-based initramfs
        GRUB_CMDLINE_LINUX="cryptdevice=/dev/$luks-disk$:luksLvmRoot root=/dev/vg0/root"

        # To systemd-based initramfs
        GRUB_CMDLINE_LINUX="rd.luks.name=$luks-disk-UUID-code$=luksLvmRoot root=/dev/vg0/root"

    Now generate the main GRUB configuration file:

        grub-mkconfig -o /boot/grub/grub.cfg

33. Install `networkmanager` package and enable `NetworkManager` service to ensure you have Internet connectivity after rebooting:

        pacman -S networkmanager
        systemctl enable NetworkManager

34. Exit new system and unmount all filesystems:

        exit
        umount -R /mnt
        swapoff -a

35. Arch is now installed 🎉. Reboot:

        reboot

36. Open BIOS settings and set `GRUB` as first boot priority. Save and exit BIOS settings. After booting the system, you should see the GRUB menu.

37. Reboot again and log in to Arch Linux with your username and password.

38. Check internet connectivity:

        ping google.com

39. Reboot!

## Post Installation

### Create Encrypted External Drive

Use cryptsetup to encrypt device:

        cryptsetup --use-urandom luksFormat /dev/<external-disk>

**Optional, just for automation:**

1. Create keyfile:

        openssl genrsa -out <path/to/key> 4096

2. Add key to encrypted device:

        cryptsetup luksAddKey /dev/<external-disk> <path/to/key>

3. Add device to /etc/crypttab for autodecrypt it:

        vim /etc/crypttab

        --> <device-name>       UUID=<device-UUID-code>      <path/to/key>    luks,<options>

        # Example don't using keyfile
        --> BACKUP      UUID=738c6426-3ef5-48d5-a837-b437c722802f       -       luks

        # Example using
        --> BACKUP      UUID=73481cae-1b80-400c-bef3-4f4a2b2a9a1e       /root/backup-key        luks

4. Add the external drive to /etc/fstab to automount (sometimes useless):

        # To help you with information about mounted drive (don't simply overwrite fstab)
        genfstab -U /

        vim /etc/fstab

        --> UUID=<device-UUID-code>     <path/to/mount> <type> <options>  <dump>  <fsck>

        # For example

        --> UUID=8d90233f-36ff-434d-bc5a-de6d596719f1       /run/timeshift/backup   ext4            rw,relatime     0 2

### Zram Implementation

1. Install the `zram-generator` package:

        pacman -S zram-generator

2. Configure zram by creating a configuration file:

        vim /etc/systemd/zram-generator.conf

        # Example configuration
        [zram0]
        zram-size = ram / 2
        compression-algorithm = lz4

3. Enable and start the zram service:

        systemctl enable systemd-zram-setup@zram0.service
        systemctl start systemd-zram-setup@zram0.service

4. Verify the zram device is active:

        swapon --show

5. Optionally, you can add the zram configuration to `/etc/fstab` for automatic setup on boot:

        echo "/dev/zram0 none swap defaults 0 0" | tee -a /etc/fstab

6. Reboot the system to apply the changes:

        reboot

### Zswap Implementation

1. Ensure the `zswap` feature is enabled in the kernel. Most modern kernels have it enabled by default. Verify by checking the kernel configuration:

        zgrep CONFIG_ZSWAP /proc/config.gz

2. Configure zswap by editing the GRUB configuration file:

        vim /etc/default/grub

    Add the following parameters to the `GRUB_CMDLINE_LINUX_DEFAULT` line:

        GRUB_CMDLINE_LINUX_DEFAULT="zswap.enabled=1 zswap.compressor=lz4 zswap.max_pool_percent=20 zswap.zpool=z3fold"

3. Update the GRUB configuration to apply the changes:

        grub-mkconfig -o /boot/grub/grub.cfg

4. Reboot the system to enable zswap with the new configuration:

        reboot

5. Verify that zswap is active by checking the kernel messages:

        dmesg | grep zswap

### Notes

#### Backup LUKS Headers

It is important to make a backup of LUKS header so that you can access your data in case of emergency (if your LUKS header somehow gets damaged).

Create a backup file:

    sudo cryptsetup luksHeaderBackup /dev/<luks-disk> --header-backup-file luks-header-backup-$(date -I)

Store the backup file in a safe place, such as a USB drive. If something bad happens, you can restore the backup header:

    sudo cryptsetup luksHeaderRestore /dev/<luks-disk> --header-backup-file /path/to/backup_header_file

## References

- https://gist.github.com/mattiaslundberg/8620837
- https://wiki.archlinux.org/index.php/Installation_guide
- https://wiki.archlinux.org/title/Dm-crypt/Encrypting_an_entire_system#LVM_on_LUKS
- https://wiki.archlinux.org/title/GRUB
- https://wiki.archlinux.org/title/Zram
- https://wiki.archlinux.org/title/Zswap
- https://joshrosso.com/docs/2020/2020-2-16-arch-windows-install/

---

Take a look at the original creator's [dotfiles repo](https://github.com/mjnaderi/dotfiles).