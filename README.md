## Termux Login V2
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/language-Python-green)
![Developer](https://img.shields.io/badge/developer-123Tool-red)

Sistem keamanan terminal Termux profesional dengan enkripsi SHA-256. Dirancang untuk memberikan perlindungan akses pada shell Termux Anda dengan fitur manajemen user yang lengkap.

## 🛡️ Fitur Utama
* **Secure Hashing:** Password dienkripsi menggunakan algoritma SHA-256 (bukan teks biasa).
* **Auto-Lock:** Terintegrasi langsung dengan sistem shell untuk perlindungan saat startup.
* **Recovery System:** Fitur pemulihan akun jika lupa password menggunakan *Security Hint*.
* **Clean Uninstaller:** Opsi untuk menghapus sistem login secara otomatis tanpa merusak sistem.
* **Anti-Bypass:** Menangani interupsi keyboard (CTRL+C) untuk mencegah akses ilegal ke terminal.

## 🚀 Instalasi

Buka Termux Anda dan jalankan perintah berikut:

```bash
pkg update && pkg upgrade
pkg install python git -y
git clone https://github.com/123tool/Termux-Login-V2.git
cd Termux-Login-V2
chmod +x setup.sh
./setup.sh
```
## Konfigurasi Manual
​Jika Anda ingin memasangnya tanpa skrip otomatis :
- Direktori
  ```
  cp login.py ~/login.py
- Bashrc
  ```
  echo "python ~/login.py" >> ~/.bashrc

## Penggunaan
- ​Saat pertama kali dijalankan, sistem akan meminta Anda melakukan Registrasi.
- ​Masukkan Username, Password, dan Security Hint (penting untuk lupa password).
- ​Untuk login selanjutnya, Anda cukup memasukkan kredensial yang telah dibuat.
- ​Pilih menu Forgot Password jika Anda kehilangan akses.

## ​⚠️ Perhatian
**​Jangan menghapus file .termux_vault.json di direktori home. File tersebut adalah database terenkripsi Anda. Jika file tersebut hilang, sistem akan menganggap tidak ada user dan meminta registrasi ulang.**
