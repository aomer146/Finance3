from modules.add_income import add_income

if __name__ == "__main__":
    try:
        amount = float(input("Gelir miktarını girin: "))
        source = input("Gelirin kaynağını girin: ")
        note = input("Not (isteğe bağlı): ")
        add_income(amount, source, note)
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin.")
