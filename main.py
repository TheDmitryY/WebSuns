from colorama import Fore
from pystyle import System
import os

author = "https://t.me/trusres"
version = "v1.0"


banner = f""" 
                                                        ▄█     █▄     ▄████████ ▀█████████▄     ▄████████ ███    █▄  ███▄▄▄▄      ▄████████ 
                                                        ███     ███   ███    ███   ███    ███   ███    ███ ███    ███ ███▀▀▀██▄   ███    ███ 
                                                        ███     ███   ███    █▀    ███    ███   ███    █▀  ███    ███ ███   ███   ███    █▀  
                                                        ███     ███  ▄███▄▄▄      ▄███▄▄▄██▀    ███        ███    ███ ███   ███   ███        
                                                        ███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀██▄  ▀███████████ ███    ███ ███   ███ ▀███████████ 
                                                        ███     ███   ███    █▄    ███    ██▄          ███ ███    ███ ███   ███          ███ 
                                                        ███ ▄█▄ ███   ███    ███   ███    ███    ▄█    ███ ███    ███ ███   ███    ▄█    ███ 
                                                        ▀███▀███▀    ██████████ ▄█████████▀   ▄████████▀  ████████▀   ▀█   █▀   ▄████████▀  
                                                                                                
                                                                                                    Author: {author} {version}
 """

menu = f"""
                    ┌────────────────────────────┐          ┌────────────────────────────┐          ┌────────────────────────────┐          ┌────────────────────────────┐
                    │          SSH Menu          ├──────────│           IP Menu          ├──────────│           Path Menu        ├──────────│         Server Menu        │
                    ├────────────────────────────┤          ├────────────────────────────┤          ├────────────────────────────┤          ├────────────────────────────┤
                    │  1. Connect (suns-laptop)  │          │   4. Scan ports            │          │   6. LAN Directory         │          │  12. Start Apache Server   │  
                    │  2. Connect (suns-pc)      │          │   5. Current IP config     │          │   7. Mobile Directory      │          │  13. Stop Apache Server    │  
                    │  3. Connect (suns-pc/suns) │          │                            │          │   8. Scripts Directory     │          │  14. Restart Apache Server │  
                    └────────────────────────────┘          └────────────────────────────┘          │   9. Downloads Directory   │          └────────────────────────────┘
                                                                                                    │   10. Music Directory      │
                                                                                                    │   11. Apache Directory     │  
                                                                                                    └────────────────────────────┘
                    """

start_menus = f"""
                                                                                    ┌────────────────────────────┐
                                                                                    │         1. Start           │
                                                                                    │         2. Exit            │         
                                                                                    └────────────────────────────┘
"""

def menus():
    System.Command("cls")
    print(Fore.LIGHTCYAN_EX + banner)
    print(Fore.LIGHTCYAN_EX + menu)
    menu_option = int(input(" > "))
    if menu_option == 1:
        System.Command("ssh manke@192.168.0.110")
    elif menu_option == 2:
        System.Command("ssh olgam@192.168.0.107")
    elif menu_option == 3:
        System.Command("ssh dimasuns@192.168.0.107")
    elif menu_option == 4:
        ip_pool = input(Fore.LIGHTCYAN_EX + "IP: ")
        System.Command(f"nmap -sV {ip_pool} ")
    elif menu_option == 5:
        System.Command("ipconfig")
    elif menu_option == 6:
        System.Command("cd /data/data/com.termux/files/home/scripts")
        System.Command("./fastpath.sh --lan")
    elif menu_option == 7:
        System.Command("cd /data/data/com.termux/files/home/scripts")
        System.Command("./fastpath.sh --sdcard")
    elif menu_option == 8:
        System.Command("cd /data/data/com.termux/files/home/scripts")
        System.Command("./fastpath.sh --scripts")
    elif menu_option == 9:
        System.Command("cd /data/data/com.termux/files/home/scripts")
        System.Command("./fastpath.sh --downloads")
    elif menu_option == 10:
        System.Command("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
    elif menu_option == 12:
        System.Command("apachectl start")
    elif menu_option == 13:
        System.Command("apachectl stop")
    elif menu_option == 14:
        System.Command("apachectl restart")
    else:
        menus()

def start_menu():
    System.Command("cls")
    print(Fore.LIGHTCYAN_EX + banner)
    print(Fore.LIGHTCYAN_EX + start_menus)
    start_option = int(input(" > "))
    if start_option == 1:
        menus()
    elif start_option == 2:
        start_menu()


if __name__ == "__main__":
    start_menu()