from modules.login import login
from modules.add_income import add_income
from modules.add_expense import add_expense
from modules.list_transactions import list_transactions
from modules.calculate_totals import calculate_totals
from modules.filter_transactions import filter_transactions
from modules.filter_by_date import filter_by_date
from modules.delete_transaction import delete_transaction
from modules.update_transaction import update_transaction
from modules.export_to_csv import export_to_csv
from modules.summarize_by_category import summarize_by_category

def main():
    if not login():
        return

    print("1. Gelir ekle")
    print("2. Gider ekle")
    print("3. Tüm işlemleri listele")
    print("4. Toplam gelir ve giderleri göster")
    print("5. Kategoriye göre filtrele")
    print("6. Tarih aralığına göre işlemleri listele")
    print("7. İşlem sil")
    print("8. İşlem güncelle")
    print("9. CSV olarak dışa aktar")
    print("10. Kategori bazlı özet rapor")

    choice = input("Seçiminizi girin (1-10): ")
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
        elif choice == "5":
            keyword = input("Filtrelemek istediğiniz kelimeyi girin: ")
            filter_transactions(keyword)
        elif choice == "6":
            start = input("Başlangıç tarihi (YYYY-MM-DD): ")
            end = input("Bitiş tarihi (YYYY-MM-DD): ")
            filter_by_date(start, end)
        elif choice == "7":
            index = int(input("Silmek istediğiniz işlemin sıra numarasını girin (1'den başlar): ")) - 1
            delete_transaction(index)
        elif choice == "8":
            index = int(input("Güncellemek istediğiniz işlemin sıra numarasını girin (1'den başlar): ")) - 1
            new_amount = float(input("Yeni miktarı girin: "))
            new_note = input("Yeni not (boş bırakmak için Enter): ")
            update_transaction(index, new_amount, new_note if new_note else None)
        elif choice == "9":
            export_to_csv()
        elif choice == "10":
            t_type = input("Gelir için 'income', Gider için 'expense' yazın: ").strip().lower()
            if t_type in ["income", "expense"]:
                summarize_by_category(t_type)
            else:
                print("❌ Geçersiz giriş.")
        else:
            print("❌ Geçersiz seçim.")
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()
