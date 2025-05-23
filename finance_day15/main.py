from modules.login import login
from modules.filter_by_month import filter_by_month

def main():
    if not login():
        return

    while True:
        print("\n📋 Ana Menü:")
        print("11. Belirli aya ait işlemleri listele")
        print("q. Çıkış")

        choice = input("Seçiminizi girin (11 veya q): ").strip().lower()

        if choice == "q":
            print("👋 Görüşmek üzere!")
            break

        if choice == "11":
            try:
                ay = int(input("Hangi aya ait işlemleri listelemek istersiniz? (1-12): "))
                filter_by_month(ay)
            except ValueError:
                print("❌ Lütfen geçerli bir sayı girin.")
        else:
            print("❌ Geçersiz seçim.")

if __name__ == "__main__":
    main()
