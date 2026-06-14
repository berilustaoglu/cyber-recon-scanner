import socket
import sys
from datetime import datetime

def banner():
    print("-" * 50)
    print("   SİBER GÜVENLİK BİLGİ TOPLAMA VE TARAMA ARACI   ")
    print("-" * 50)

def ip_bul(hedef_url):
    try:
        # URL'den "http://" veya "https://" kısımlarını temizleme
        temiz_url = hedef_url.replace("https://", "").replace("http://", "").split('/')[0]
        ip = socket.gethostbyname(temiz_url)
        print(f"[+] Hedef IP Adresi: {ip}")
        return ip
    except socket.gaierror:
        print("[-] Hata: IP adresi çözümlenemedi. URL'yi kontrol edin.")
        sys.exit()

def port_tara(hedef_ip):
    # En kritik siber güvenlik portları
    portlar = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 3389: "RDP"}
    
    print(f"\n[*] Tarama başladı: {datetime.now().strftime('%H:%M:%S')}")
    print("[*] Kritik portlar taranıyor...\n")
    
    for port, servis in portlar.items():
        # TCP bağlantısı oluşturma (Bağlantı süresini 1 saniye ile sınırladık)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        sonuc = s.connect_ex((hedef_ip, port))
        if sonuc == 0:
            print(f"[+] Port {port} ({servis}): AÇIK 🟢")
        else:
            print(f"[-] Port {port} ({servis}): Kapalı 🔴")
        s.close()

if __name__ == "__main__":
    banner()
    hedef = input("Hedef URL veya IP girin (Örn: google.com): ")
    
    # 1. Aşama: IP Bulma
    hedef_ip = ip_bul(hedef)
    
    # 2. Aşama: Port Tarama
    port_tara(hedef_ip)
    print("\n[+] Tarama tamamlandı!")
