import subprocess
import sys
import os
import time
import json
from colorama import Back, Fore, init, Style

init(autoreset=True)
settings_file = "settings.json"
password = ""
config = ""

def first_login():
    global password, config
    password = input("Enter new sudo password: ")
    config = input("Enter new config name: ")
    save_settings()
    clear_screen()
    
def getinfo():
    print('''
    Works on linux only!

    If you have any improvement idea contact: io1n@proton.me
    For more information go to README.md
          ''')
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading(message):
    print(message, end='', flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print()

def save_settings():
    with open(settings_file, "w") as f:
        json.dump({"password": password, "config": config}, f)

def load_settings():
    global password, config
    if os.path.exists(settings_file):
        with open(settings_file, "r") as f:
            data = json.load(f)
            password = data.get("password", "")
            config = data.get("config", "")
    else:
        first_login()

def Up():
    loading(f"Turning on {config}")
    subprocess.run(
        ["sudo", "-S", "wg-quick", "up", config],
        input=password + "\n",
        text=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print(f"VPN {config} is ON\n")

def Dw():
    loading(f"Turning off {config}")
    subprocess.run(
        ["sudo", "-S", "wg-quick", "down", config],
        input=password + "\n",
        text=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print(f"VPN {config} is OFF\n")

def ext():
    print("Exiting...")
    sys.exit()

def menu():
    print(Fore.RED + Style.BRIGHT + r'''
__        ___                                    _ 
\ \      / (_)_ __ ___  __ _ _   _  __ _ _ __ __| |
 \ \ /\ / /| | '__/ _ \/ _` | | | |/ _` | '__/ _` |
  \ V  V / | | | |  __/ (_| | |_| | (_| | | | (_| |
   \_/\_/  |_|_|  \___|\__, |\__,_|\__,_|_|  \__,_|
                       |___/                       

    ''')
    print(f'Current config: {config}')
    print('''
Choose option:
[1] Turn on VPN
[2] Turn off VPN
[3] Change settings
[4] Info
[5] Exit
    ''')

def change_settings():
    global password, config
    print('''
    Choose option:
    [1] Change password
    [2] Change config
    [3] Back to main menu
    ''')
    optc = int(input('Enter choice: '))
    if optc == 1:
        password = input("Enter new sudo password: ")
        save_settings()
        clear_screen()
        print("Password updated!\n")
        time.sleep(1)
    elif optc == 2:
        config = input("Enter new config name: ")
        save_settings()
        clear_screen()
        print(f"Config updated! Current config: {config}\n")
        time.sleep(1)
    elif optc == 3:
        clear_screen()
    else:
        print("Invalid choice!")
        time.sleep(1)
        clear_screen()

def act(opt):
    match opt:
        case 1:
            Up()
        case 2:
            Dw()
        case 3:
            change_settings()
        case 4:
            getinfo()
        case 5:
            ext()
        case _:
            print(Fore.RED + "Invalid choice!\n")

load_settings()

while True:
    menu()
    try:
        opt = int(input("Enter choice: "))
        act(opt)
        time.sleep(1)
        clear_screen()
    except ValueError:
        print(Fore.RED + "Invalid choice!\n")
        time.sleep(1)
        clear_screen()

