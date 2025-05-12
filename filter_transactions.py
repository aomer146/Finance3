import json
import os

DATA_PATH = os.path.join("data", "transactions.json")

def filter_transactions(keyword):
    if not os.path.exists(DATA_PATH):
        print("📁 Veri dosyası bulunamadı.")
        return

    with open(DATA_PATH, "r") as f:
        transactions = json.load(f)

    found = False
    for t in transactions:
        combined = t.get("source", "") + t.get("category", "") + t.get("note", "")
        if keyword.lower() in combined.lower():
            found = True
            print(f"[{t['type'].upper()}] {t['amount']}₺ - {t.get('source', t.get('category', ''))} - {t['note']} - {t['date']}")

    if not found:
        print("🔍 Eşleşen kayıt bulunamadı.")
