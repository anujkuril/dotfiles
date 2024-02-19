#!/bin/sh
#
wal -R &
nm-applet &
kdeconnect-indicator &
dunst &
picom & 
copyq &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

MOUSE_ID=$(xinput --list --short | grep -i touchpad| cut -d "=" -f2 | cut -c 1-2)
accel=$(xinput --list-props "$MOUSE_ID" | grep 'Accel Speed' | cut -d "(" -f2 | cut -c 1-3 | tail -2 | head -1)
Tap=$(xinput --list-props "$MOUSE_ID" | grep 'Tapping Enabled' | cut -d "(" -f2 | cut -c 1-3 | tail -2 | head -1)
xinput --set-prop "$MOUSE_ID" "$accel" 0.5
xinput --set-prop "$MOUSE_ID" "$tap" 1
