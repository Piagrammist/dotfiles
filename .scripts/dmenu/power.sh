#!/bin/sh

choice=$(printf "󰐥 Power Off\n Restart\n󰤄 Suspend\n Log out" | rofi -dmenu -i  -l 4 -p "PowerMenu")

case "$choice" in
    " Restart")    reboot            ;;
    "󰐥 Power Off")  shutdown    now   ;;
    "󰤄 Suspend")    systemctl suspend ;;
    " Log out")    killall    qtile  ;;
    *) exit 1 ;;
esac
