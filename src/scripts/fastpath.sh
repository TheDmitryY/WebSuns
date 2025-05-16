#!/bin/bash

help_menu() {
        echo "  Використання:"
        echo "   ./fastpath.sh <параметр> "
        echo "      --lan - Перейти в локальну папку "
        echo "      --sdcard - Перейти в память телефону "
        echo "      --scripts - Перейти в папку зі скриптами"
	echo "	    --music - Перейти в папку зі музикою"
	echo "	    --downloads - Перейти в папку завантаження"
}

if [[ "$1" == "--lan" ]]; then
	cd /sdcard/LAN && ls
	exit 0
elif [[ "$1" == "--sdcard" ]]; then
	cd /sdcard && ls
	exit 0
elif [[ "$1" == "--scripts" ]]; then
	cd /data/data/com.termux/files/home/scripts && ls
	exit 0
elif [[ "$1" == "--help" ]]; then
	help_menu
	exit 0
elif [[ "$1" == "--music" ]]; then
	cd /sdcard/music && ls
	exit 0
elif [[ "$1" == "--download" ]]; then
	cd /sdcard/dowload
	exit 0
else
	echo "Команда не введена!"
	echo ""
	help_menu

fi

