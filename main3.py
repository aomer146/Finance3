
from modules.add_income import add_income
from modules.add_expense import add_expense
from modules.view_transactions import load_transactions, list_transactions, search_transactions

def main():
    print("1. Gelir ekle")
    print("2. Gider ekle")
    print("3. İşlemleri listele")
    print("4. İşlem ara")
    choice = input("Seçiminizi girin (1/2/3/4): ")

    if choice in ["1", "2"]:
        try:
            amount = float(input("Miktarı girin: "))
            note = input("Not (isteğe bağlı): ")

            if choice == "1":
                source = input("Gelirin kaynağını girin: ")
                add_income(amount, source, note)
            elif choice == "2":
                category = input("Giderin kategorisini girin: ")
                add_expense(amount, category, note)
        except ValueError:
            print("❌ Lütfen geçerli bir sayı girin.")
    elif choice == "3":
        transactions = load_transactions()
        list_transactions(transactions)
    elif choice == "4":
        transactions = load_transactions()
        keyword = input("Aranacak kelimeyi girin: ")
        search_transactions(transactions, keyword)
    else:
        print("❌ Geçersiz seçim.")

if __name__ == "__main__":
    main()
