# Simple Cybersecurity Recon & Port Scanner

A lightweight, fast, and dependency-free Python tool designed to automate the initial reconnaissance and port scanning phases of a penetration test.

## 🚀 Features
- **IP Resolution:** Automatically resolves the target domain name into its corresponding IP address.
- **Critical Port Scanning:** Quickly scans the top 5 most critical network ports (21, 22, 80, 443, 3389).
- **Zero Dependencies:** Built entirely using Python's standard libraries (`socket`, `sys`, `datetime`).

## 🛠️ Target Ports & Services
- **Port 21:** FTP (File Transfer Protocol)
- **Port 22:** SSH (Secure Shell)
- **Port 80:** HTTP (Web Traffic)
- **Port 443:** HTTPS (Secure Web Traffic)
- **Port 3389:** RDP (Remote Desktop Protocol)

## 💻 Usage

1. Clone this repository or download the source code:
```bash
git clone https://github.com
cd cyber-recon-scanner
```

2. Run the script using Python 3:
```bash
python cyber_scanner.py
```

3. Enter the target domain (e.g., `example.com`) when prompted.

## ⚠️ Disclaimer
This tool is developed strictly for educational purposes and authorized penetration testing. Scanning targets without prior written consent is illegal and the user assumes all responsibility for any misuse of this software.
