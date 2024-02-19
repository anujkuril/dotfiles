#!/bin/sh
#
wal -R &
nm-applet &
kdeconnect-indicator &
dunst &
picom & 
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
swww-daemon &
swww init &

