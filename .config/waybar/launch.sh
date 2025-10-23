#!/bin/bash

# Kill waybar
killall waybar
pkill waybar
sleep 0.5

# Reload ags
ags quit &
sleep 0.2
ags run &

# Load waybar
waybar &
