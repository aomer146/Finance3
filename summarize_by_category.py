import json
import os

DATA_PATH = os.path.join("data/transactions.json")

def summarize_by_category(transaction_type):
    if not os.path.exists(DATA_PATH):
        print("📁 Veri dosyası bulunamadı.")
        return

    with open(DATA_PATH, "r") as f:
        transactions = json.load(f)

    summary = {}

    for t in transactions:
        if t["type"] == transaction_type:
            key = t.get("category") if transaction_type == "expense" else t.get("source")
            if key:
                summary[key] = summary.get(key, 0) + t["amount"]

    if not summary:
        print("🔍 Kayıt bulunamadı.")
        return

    print(f"📊 {transaction_type.upper()} Özet Raporu:")
    for key, total in summary.items():
        print(f"- {key}: {total}₺")
