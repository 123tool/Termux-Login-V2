#!/bin/bash

# ==========================================
# Termux Login V2 - Auto Installer
# Developer: 123Tool & SPY-E
# ==========================================

# Warna untuk output terminal
G='\033[0;32m'
B='\033[0;34m'
Y='\033[1;33m'
R='\033[0;31m'
X='\033[0m'

clear
echo -e "${B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${X}"
echo -e "${G}         INSTALLER: TERMUX LOGIN VAULT         ${X}"
echo -e "${B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${X}"
echo -e "${Y}[*] Developed by: 123Tool${X}"
echo ""

# Step 1: Cek Dependensi
echo -e "${G}[+]${X} Mengecek dependensi..."
if ! command -v python &> /dev/null; then
    echo -e "${Y}[!]${X} Python tidak ditemukan. Menginstal..."
    pkg install python -y
else
    echo -e "${G}[*]${X} Python sudah terpasang."
fi

# Step 2: Cek File Sumber
if [ ! -f "login.py" ]; then
    echo -e "${R}[!] Error: File login.py tidak ditemukan di folder ini!${X}"
    echo -e "${Y}[i] Pastikan Anda berada di direktori yang benar.${X}"
    exit 1
fi

# Step 3: Menyalin Script ke Home
echo -e "${G}[+]${X} Menyalin script keamanan ke direktori home..."
cp login.py $HOME/login.py
chmod +x $HOME/login.py

# Step 4: Integrasi ke Startup (.bashrc)
echo -e "${G}[+]${X} Mengonfigurasi shell startup..."
BASHRC="$HOME/.bashrc"

# Jika belum ada line login, tambahkan
if ! grep -q "python ~/login.py" "$BASHRC"; then
    echo "python ~/login.py" >> "$BASHRC"
    echo -e "${G}[*]${X} Berhasil mendaftarkan login ke .bashrc"
else
    echo -e "${Y}[!]${X} Konfigurasi sudah ada di .bashrc, melewati langkah ini."
fi

# Selesai
echo -e "${B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${X}"
echo -e "${G}       PROSES INSTALASI BERHASIL DISUKSES      ${X}"
echo -e "${B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${X}"
echo -e "${Y}[!] Silakan restart Termux atau ketik: source ~/.bashrc${X}"
echo ""
