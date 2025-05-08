from modules.add_income import add_income
from modules.add_expense import add_expense
from modules.list_transactions import list_transactions

def main():
    print("1. Gelir ekle")
    print("2. Gider ekle")
    print("3. Tüm işlemleri listele")

    choice = input("Seçiminizi girin (1/2/3): ")

    try:
        if choice == "1":
            amount = float(input("Miktarı girin: "))
            source = input("Gelirin kaynağını girin: ")
            note = input("Not (isteğe bağlı): ")
            add_income(amount, source, note)
        elif choice == "2":
            amount = float(input("Miktarı girin: "))
            category = input("Giderin kategorisini girin: ")
            note = input("Not (isteğe bağlı): ")
            add_expense(amount, category, note)
        elif choice == "3":
            list_transactions()
        else:
            print("❌ Geçersiz seçim.")
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()
