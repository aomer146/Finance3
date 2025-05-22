
import json
import os

DATA_PATH = os.path.join("data", "transactions.json")

def load_transactions():
    if not os.path.exists(DATA_PATH):
        print("❌ Veri dosyası bulunamadı.")
        return []

    with open(DATA_PATH, "r") as f:
        return json.load(f)

def list_transactions(transactions):
    income_total = 0
    expense_total = 0

    print("\n--- Gelir ve Giderler ---")
    for t in transactions:
        if t['type'] == 'income':
            income_total += t['amount']
            print(f"Gelir: {t['amount']} TL | {t['source']} | {t['note']} | {t['date']}")
        elif t['type'] == 'expense':
            expense_total += t['amount']
            print(f"Gider: {t['amount']} TL | {t['category']} | {t['note']} | {t['date']}")

    print(f"\nToplam Gelir: {income_total} TL")
    print(f"Toplam Gider: {expense_total} TL")
    print(f"Bakiye: {income_total - expense_total} TL")

def search_transactions(transactions, keyword):
    found = False
    for t in transactions:
        if keyword.lower() in (t.get("note", "").lower() + t.get("source", "").lower() + t.get("category", "").lower()):
            found = True
            print(f"{t['date']} | {t['type'].upper()} | {t['amount']} TL | {t.get('source', t.get('category', ''))} | {t['note']}")
    
    if not found:
        print("❌ Arama kriterine uygun işlem bulunamadı.")
