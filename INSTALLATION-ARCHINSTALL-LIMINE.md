# Installation Guide

1. Install yout system with `archinstall`

    ```bash
    # archinstall
    ```

    and reach this config (from Omarchy):

    | Section                         | Option                                                                    |
    |---------------------------------|---------------------------------------------------------------------------|
    | Mirrors and repositories        | Select regions > Your country                                             |
    | Disk configuration              | Partitioning > Default partitioning layout > Select disk (space + enter)  |
    | Disk > File system              | btrfs (default structure: yes + use compression)                          |
    | Disk > Disk encryption          | Encryption type: LUKS + Encryption password + Partitions (select the one) |
    | Hostname                        | Give your computer a name                                                 |
    | Bootloader                      | Limine                                                                    |
    | Authentication > Root password  | Set yours                                                                 |
    | Authentication > User account   | Add a user > Superuser: Yes > Confirm and exit                            |
    | Applications > Audio            | pipewire                                                                  |
    | Network configuration           | Copy ISO network config                                                   |
    | Timezone                        | Set yours                                                                 |

2. Install git and vim

    ```bash
    # pacman -Syu git vim
    ```

3. Download and install yay package

    ```bash
    git clone https://aur.archlinux.org/yay.git

    cd yay

    makepkg -si
    ```

4. Install limine auxiliar packages

    ```bash
    # pacman -S jdk-openjdk

    $ yay -S limine-mkinitcpio-hook
    ```

5. Generate initial configs

    ```bash
    # cp /etc/limine-entry-tool.conf /etc/default/limine

    # limine-update
    ```

6. Configurate `default-entry`:

    ```bash
    # vim /boot/limine.conf

    # default_entry: 2 ---> 3
    ```

7. Add `btrfs-overlayfs` after `filesystems` in HOOKS=(...) on mkinitcpio config

    ```bash
    # vim /etc/mkinitcpio.conf

    HOOKS=(... filesystems btrfs-overlayfs)

    # limine-update
    ```

8. Install and enable limine-snapper-sync

    ```bash
    $ yay -S limine-snapper-sync

    # systemctl enable --now limine-snapper-sync.service
    ```

9. Enable `snapper-timelist`

    ```bash
    # systemctl enable --now snapper-timeline.timer
    ```

10. Enable snapper-cleanup.service

    ```bash
    # systemctl enable --now snapper-cleanup.timer
    ```

11. Add `snapper-timeline` config

    ```
    /etc/snapper/configs/<config>

    TIMELINE_MIN_AGE="1800"
    TIMELINE_LIMIT_HOURLY="5"
    TIMELINE_LIMIT_DAILY="7"
    TIMELINE_LIMIT_WEEKLY="0"
    TIMELINE_LIMIT_MONTHLY="0"
    TIMELINE_LIMIT_YEARLY="0"
    ```

12. Install and enable `snap-pac` (automatic snapshots during updates)

    ```bash
    # pacman -Syu snap-pac
    ```
