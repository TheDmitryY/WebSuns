from colorama import Fore, init
from pystyle import System
import os
import platform

author = "https://t.me/trusres"
version = "v1.1"


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

def system_check():
    global system_os
    system_os = platform.system()

def clear_cmd():
    system_check()
    if system_os == "Windows":
        System.Command("cls")
    elif system_os == "Linux":
        System.Command("clear")

def repeat_programm():
    print(Fore.LIGHTGREEN_EX + "\n[] Wanna reapeat? [Yes/No]")
    rep_option = str(input(Fore.LIGHTGREEN_EX + " > " + Fore.RESET))
    if rep_option == "Yes":
        menus()
    else:
        clear_cmd()
        exit

def menus():
    system_check()
    clear_cmd()

    print(Fore.LIGHTCYAN_EX + banner)
    print(Fore.LIGHTCYAN_EX + menu)
    
    menu_option = int(input(" > "))
    if menu_option == 1:
        System.Command("ssh manke@192.168.0.110")
        repeat_programm()

    elif menu_option == 2:
        System.Command("ssh olgam@192.168.0.107")
        repeat_programm()
    
    elif menu_option == 3:
        System.Command("ssh dimasuns@192.168.0.107")
        repeat_programm()
    
    elif menu_option == 4:
        ip_pool = input(Fore.LIGHTCYAN_EX + "IP: ")
        System.Command(f"nmap -sV {ip_pool} ")
        repeat_programm()

    elif menu_option == 5:
        clear_cmd()
        if system_os == "Windows":
            System.Command("ipconfig")
            repeat_programm()
        elif system_os == "Linux":
            System.Command("ifconfig")
            repeat_programm()
        else:
            print(Fore.LIGHTRED_EX + "[ERROR] Your operation system dont supported!" + Fore.RESET)
            repeat_programm()
    
    elif menu_option == 6:
        if system_os == "Windows":
            print(Fore.LIGHTRED_EX + "[ERROR] This option dont support on Windows system" + Fore.RESET)
            repeat_programm()
        else:
            System.Command("cd src/scripts")
            System.Command("bash fastpath.sh --lan")
            repeat_programm()
    
    elif menu_option == 7:
        if system_os == "Windows":
            print(Fore.LIGHTRED_EX + "[ERROR] This option dont support on Windows system" + Fore.RESET)
            repeat_programm()
        else:
            System.Command("cd src/scripts")
            System.Command("bash fastpath.sh --sdcard")
            repeat_programm()
    
    elif menu_option == 8:
        if system_os == "Windows":
            print(Fore.LIGHTRED_EX + "[ERROR] This option dont support on Windows system" + Fore.RESET)
            repeat_programm()
        else:
            System.Command("cd src/scripts")
            System.Command("bash fastpath.sh --scripts")
            repeat_programm()
    
    elif menu_option == 9:
        if system_os == "Windows":
            print(Fore.LIGHTRED_EX + "[ERROR] This option dont support on Windows system" + Fore.RESET)
            repeat_programm()
        else:
            System.Command("cd src/scripts")
            System.Command("bash fastpath.sh --downloads")
            repeat_programm()
    
    elif menu_option == 10:
        System.Command("cd /data/data/com.termux/files/usr/share/apache2/default-site/htdocs")
        repeat_programm()
    
    elif menu_option == 12:
        System.Command("apachectl start")
        repeat_programm()
    
    elif menu_option == 13:
        System.Command("apachectl stop")
        repeat_programm()
    
    elif menu_option == 14:
        System.Command("apachectl restart")
        repeat_programm()
    else:
        menus()

def start_menu():
    clear_cmd()
    print(Fore.LIGHTCYAN_EX + banner)
    print(Fore.LIGHTCYAN_EX + start_menus)
    start_option = int(input(" > "))
    if start_option == 1:
        menus()
    elif start_option == 2:
        clear_cmd()
        exit


if __name__ == "__main__":
    start_menu()