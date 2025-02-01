import hashlib
import datetime

# Lisans anahtarı ve kullanıcı bilgileri
licenses = {
    "1234-5678-ABCD-EFGH": {
        "username": "Ali Yılmaz",
        "expiration_date": "2025-12-31"
    },
    "9876-5432-ZYXW-VUTS": {
        "username": "Ayşe Demir",
        "expiration_date": "2025-06-30"
    }
}

# Lisans anahtarını doğrulayan fonksiyon
def validate_license(license_key):
    license_info = licenses.get(license_key)
    if license_info:
        expiration_date = datetime.datetime.strptime(license_info["expiration_date"], "%Y-%m-%d")
        if expiration_date >= datetime.datetime.now():
            return license_info
        else:
            print("Lisans süresi dolmuş.")
            return None
    else:
        print("Geçersiz lisans anahtarı.")
        return None

# Ascii Art
def display_ascii_art():
    art = '''
 ____             _      ____                      
|  _ \\  __ _ _ __| | __ |  _ \\ _ __ _____  ___   _ 
| | | |/ _` | '__| |/ / | |_) | '__/ _ \\ \/ / | | |
| |_| | (_| | |  |   <  |  __/| | | (_) >  <| |_| |
|____/ \\__,_|_|  |_\\_\\ |_|   |_|  \\___/_/\\_\\\\__, |
                                             |___/  
'''
    print(art)

# Kullanıcıdan lisans anahtarını al
def get_license():
    license_key = input("Lütfen lisans anahtarınızı girin: ")
    return license_key

# Menü
def show_menu(username):
    print(f"\nHoş geldiniz, {username}!")
    print("1. Programı Başlat")
    print("2. Çıkış")
    choice = input("Seçiminiz: ")
    if choice == "1":
        print("Program başlatılıyor...")
    elif choice == "2":
        print("Çıkış yapılıyor...")
    else:
        print("Geçersiz seçim!")

# Renkli metin için ANSI kodları
def colored_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color, colors['white'])}{text}{colors['reset']}"

# Ana fonksiyon
def main():
    # Başlık
    print(colored_text("Dark Proxy", 'blue'))
    display_ascii_art()

    # Lisans anahtarını al
    license_key = get_license()

    # Lisans doğrulaması
    license_info = validate_license(license_key)

    if license_info:
        show_menu(license_info["username"])
    else:
        print("Programa giriş yapılamaz.")

if __name__ == "__main__":
    main()
