use nupm/modules/nupm

source "./scripts/custom-completions/git/git-completions.nu"

$env.config.show_banner = false

alias l = ls -a
alias ll = ls -al
alias lf = ls -af
alias lt = eza --tree -alh