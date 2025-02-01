import hashlib

# Lisans anahtarını doğrulayan fonksiyon
def validate_license(license_key):
    # Lisans anahtarı burada saklanabilir, örnek için sabit bir değer kullanıyoruz
    valid_license = "1234-5678-ABCD-EFGH"
    
    # Lisans anahtarını doğrula
    if license_key == valid_license:
        return True
    else:
        return False

# Kullanıcıdan lisans anahtarını al
def get_license():
    license_key = input("Lütfen lisans anahtarınızı girin: ")
    return license_key

def main():
    # Lisans anahtarını al
    license_key = get_license()
    
    # Lisans doğrulaması
    if validate_license(license_key):
        print("Lisans doğrulandı! Programa hoş geldiniz.")
        # Burada programın geri kalan kısmı çalıştırılabilir
    else:
        print("Geçersiz lisans anahtarı. Programa giriş yapılamaz.")

if __name__ == "__main__":
    main()
