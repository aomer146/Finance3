import json
import os
import csv

DATA_PATH = os.path.join("data/transactions.json")
EXPORT_PATH = os.path.join("data", "transactions_export.csv")

def export_to_csv():
    if not os.path.exists(DATA_PATH):
        print("📁 Kayıtlı veri bulunamadı.")
        return

    with open(DATA_PATH, "r") as f:
        transactions = json.load(f)

    if not transactions:
        print("📂 Hiç kayıt bulunamadı.")
        return

    with open(EXPORT_PATH, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["type", "amount", "source", "category", "note", "date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for t in transactions:
            writer.writerow({
                "type": t.get("type", ""),
                "amount": t.get("amount", ""),
                "source": t.get("source", ""),
                "category": t.get("category", ""),
                "note": t.get("note", ""),
                "date": t.get("date", "")
            })

    print(f"✅ CSV olarak dışa aktarıldı: {EXPORT_PATH}")
