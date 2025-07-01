use custom-completions *

# Load the theme
source "./scripts/themes/nu-themes/dracula.nu"

# Aliases
alias l = ls -a
alias ll = ls -al
alias lf = ls -af
alias lt = eza --tree -alh


# Prompt
$env.PROMPT_INDICATOR = ""
$env.PROMPT_MULTILINE_INDICATOR = ""
$env.PROMPT_COMMAND = {
    let home_path = $env.HOME
    let current_path = $env.PWD

    let prompt_string = if $current_path == $home_path {
        $"(ansi '#ffffff')[ (ansi '#ffff00')~(ansi '#ffffff') ]"
    } else {
        $"(ansi '#ffffff')[ (ansi '#ffff00')($current_path) (ansi '#ffffff')]"
    }

    $"($prompt_string) -> "
}


$env.config.show_banner = false