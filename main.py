from kullanici import kullanici_ekle, giris_yap
from kategori import kategori_ekle, kategorileri_getir
from islem import islem_ekle, islemleri_getir
from tarih_filtrele import islemleri_tarihe_gore_getir

def menu():
    print("\n1. Kullanıcı Ekle")
    print("2. Giriş Yap")
    print("3. Kategori Ekle")
    print("4. İşlem Ekle")
    print("5. Tüm İşlemleri Listele")
    print("6. Tarihe Göre Filtrele")
    print("0. Çıkış")

def main():
    while True:
        menu()
        secim = input("Seçiminiz: ")
        if secim == "1":
            username = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            kullanici_ekle(username, password)
        elif secim == "2":
            username = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            user = giris_yap(username, password)
            print("Giriş başarılı." if user else "Hatalı giriş.")
        elif secim == "3":
            ad = input("Kategori adı: ")
            kategori_ekle(ad)
        elif secim == "4":
            user_id = int(input("Kullanıcı ID: "))
            category_id = int(input("Kategori ID: "))
            amount = float(input("Tutar: "))
            date = input("Tarih (YYYY-MM-DD): ")
            desc = input("Açıklama: ")
            islem_ekle(user_id, category_id, amount, date, desc)
        elif secim == "5":
            for i in islemleri_getir():
                print(dict(i))
        elif secim == "6":
            start = input("Başlangıç tarihi (YYYY-MM-DD): ")
            end = input("Bitiş tarihi (YYYY-MM-DD): ")
            for i in islemleri_tarihe_gore_getir(start, end):
                print(dict(i))
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
