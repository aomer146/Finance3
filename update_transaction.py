import json
import os
from datetime import datetime
DATA_PATH = os.path.join("data", "transactions.json")
def update_transaction(index, new_amount=None, new_note=None):
    if not os.path.exists(DATA_PATH):
        print("📁 Veri dosyası bulunamadı.")
        return
    with open(DATA_PATH, "r") as f:
        transactions = json.load(f)
    if not (0 <= index < len(transactions)):
        print("❌ Geçersiz işlem numarası.")
        return
    if new_amount is not None:
        transactions[index]["amount"] = new_amount
    if new_note is not None:
        transactions[index]["note"] = new_note
    transactions[index]["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_PATH, "w") as f:
        json.dump(transactions, f, indent=4)
    print("✅ İşlem güncellendi.")
