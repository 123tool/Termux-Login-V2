import os
import json
import hashlib
import sys
import time

# Konfigurasi & Developer Info
DEV = "123Tool"
DB_FILE = os.path.expanduser("~/.termux_vault.json")

# Colors
R = "\033[31m"  # Red
G = "\033[32m"  # Green
Y = "\033[33m"  # Yellow
B = "\033[34m"  # Blue
C = "\033[36m"  # Cyan
W = "\033[37m"  # White
X = "\033[0m"   # Reset

def clear():
    os.system('clear')

def banner():
    ascii_art = f"""
    {C}      __________________________
    {C}     /                          \\
    {C}    |    {W}SECURITY GATEWAY v1.0{C}   |
    {C}    |    {Y}Restricted Access{C}       |
    {C}     \\__________________________/
    {C}                |  |
    {W}          ______[  ]______
    {W}         /                \\
    {W}        |  [7] [8] [9]     |
    {W}        |  [4] [5] [6]     |
    {W}        |  [1] [2] [3]     |
    {W}        |      [0]         |
    {W}         \\________________/
    
    {B}      Developed by: {DEV}
    {X}"""
    print(ascii_art)

def make_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def register():
    clear()
    banner()
    db = load_db()
    if "user" in db:
        print(f"{R}[!] User sudah terdaftar. Gunakan opsi Reset atau Login.")
        time.sleep(2)
        return

    print(f"{G}[+] --- Registration Phase ---")
    user = input(f"{W}Set Username: ")
    pw = input(f"{W}Set Password: ")
    hint = input(f"{W}Security Hint (for recovery): ")
    
    db["user"] = user
    db["pass"] = make_hash(pw)
    db["hint"] = hint
    save_db(db)
    print(f"\n{G}[*] Success! Restart Termux to apply.")
    sys.exit()

def login():
    db = load_db()
    if "user" not in db:
        register()
    
    attempts = 0
    while attempts < 3:
        clear()
        banner()
        print(f"{Y}[*] Please Login to access terminal")
        u = input(f"{W}Username: ")
        p = input(f"{W}Password: ")

        if u == db["user"] and make_hash(p) == db["pass"]:
            print(f"\n{G}[+] Access Granted. Welcome, {u}!")
            time.sleep(1)
            clear()
            break
        else:
            attempts += 1
            print(f"\n{R}[!] Invalid Credentials! ({attempts}/3)")
            time.sleep(1.5)
    else:
        print(f"\n{R}[!] Too many failed attempts. Locking...")
        sys.exit()

def forgot_login():
    clear()
    banner()
    db = load_db()
    if not db:
        print(f"{R}[!] No account found.")
        return

    print(f"{Y}[?] Recovery Mode")
    ans = input(f"{W}Security Hint Answer: ")
    if ans == db["hint"]:
        new_pw = input(f"{G}Enter New Password: ")
        db["pass"] = make_hash(new_pw)
        save_db(db)
        print(f"{G}[*] Password updated successfully!")
    else:
        print(f"{R}[!] Wrong hint!")
    time.sleep(2)

def remove_login():
    clear()
    banner()
    db = load_db()
    pw = input(f"{R}[!] Enter password to confirm removal: ")
    if make_hash(pw) == db.get("pass"):
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)
        # Menghapus hook di .bashrc
        bashrc = os.path.expanduser("~/.bashrc")
        if os.path.exists(bashrc):
            with open(bashrc, "r") as f:
                lines = f.readlines()
            with open(bashrc, "w") as f:
                for line in lines:
                    if "login.py" not in line:
                        f.write(line)
        print(f"{G}[*] Login system removed.")
        sys.exit()
    else:
        print(f"{R}[!] Unauthorized.")
    time.sleep(2)

def main_menu():
    while True:
        clear()
        banner()
        print(f"{W}1. Login to Terminal")
        print(f"{W}2. Forgot Password")
        print(f"{W}3. Uninstall Login")
        print(f"{W}4. Exit")
        
        opt = input(f"\n{C}Selection > {X}")
        
        if opt == "1": login(); break
        elif opt == "2": forgot_login()
        elif opt == "3": remove_login()
        elif opt == "4": sys.exit()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Forbidden exit.")
        sys.exit()
