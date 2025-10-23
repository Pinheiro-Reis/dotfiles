use std/util "path add"
path add "~/.local/bin"

$env.NU_LIB_DIRS = ($env.NU_LIB_DIRS | append ($nu.config-path | path dirname | path join 'scripts'))