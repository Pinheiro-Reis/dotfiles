#INSTALL
Use stow and, if necessary, rename actual config file (stow don't overwrites nothing, just adopt, but becareful)

## PACMAN

    # to update
    pacman -Qeq > DOCS/PACKAGES

    # to install
    pacman -S --needed - < DOCS/PACKAGES

## FLATPAK

    # to update
    flatpak list --columns=application --app > DOCS/PACKAGES-FLATPAK

    # to install
    xargs flatpak --user install -y < DOCS/PACKAGES-FLATPAK

NOTES

1. Waybar workspaces are bugged with an extra white background in button:hover (under mouse option)

ATRIBUITION

-   The ML4W Dotfiles for Hyprland <https://github.com/mylinuxforwork/dotfiles.git>
-   The Mjnaderi for installation script <https://gist.github.com/mjnaderi/28264ce68f87f52f2cabb823a503e673>
