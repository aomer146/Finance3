from modules.add_income import add_income
from modules.add_expense import add_expense
from modules.list_transactions import list_transactions
from modules.calculate_totals import calculate_totals

def main():
    print("1. Gelir ekle")
    print("2. Gider ekle")
    print("3. Tüm işlemleri listele")
    print("4. Toplam gelir ve giderleri göster")
    choice = input("Seçiminizi girin (1/2/3/4): ")

    try:
        if choice in ["1", "2"]:
            amount = float(input("Miktarı girin: "))
            note = input("Not (isteğe bağlı): ")

        if choice == "1":
            source = input("Gelirin kaynağını girin: ")
            add_income(amount, source, note)
        elif choice == "2":
            category = input("Giderin kategorisini girin: ")
            add_expense(amount, category, note)
        elif choice == "3":
            list_transactions()
        elif choice == "4":
            calculate_totals()
        else:
            print("❌ Geçersiz seçim.")
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()
