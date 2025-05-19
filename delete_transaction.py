import json
import os
DATA_PATH = os.path.join("data", "transactions.json")
def delete_transaction(index):
    if not os.path.exists(DATA_PATH):
        print("📁 Veri dosyası bulunamadı.")
        return
    with open(DATA_PATH, "r") as f:
        transactions = json.load(f)
    if not (0 <= index < len(transactions)):
        print("❌ Geçersiz işlem numarası.")
        return
    deleted = transactions.pop(index)
    with open(DATA_PATH, "w") as f:
        json.dump(transactions, f, indent=4)
    print(f"🗑 Silindi: [{deleted['type'].upper()}] {deleted['amount']}₺ - {deleted.get('source', deleted.get('category', ''))}")
