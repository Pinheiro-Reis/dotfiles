#!/bin/bash

set -e

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

if [ -z "$1" ]; then
  echo "Usage: $0 <path_to_wallpaper>"
  exit 1
fi

WALLPAPER_PATH="$1"
hyprctl hyprpaper reload ,"$WALLPAPER_PATH"
