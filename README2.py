from modules.add_income import add_income
from modules.add_expense import add_expense

def main():
    print("1. Gelir ekle")
    print("2. Gider ekle")
    choice = input("Seçiminizi girin (1/2): ")

    try:
        amount = float(input("Miktarı girin: "))
        if choice == "1":
            source = input("Gelirin kaynağını girin: ")
            note = input("Not (isteğe bağlı): ")
            add_income(amount, source, note)
        elif choice == "2":
            category = input("Giderin kategorisini girin: ")
            note = input("Not (isteğe bağlı): ")
            add_expense(amount, category, note)
        else:
            print("❌ Geçersiz seçim.")
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()
