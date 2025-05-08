import json
import os

DATA_PATH = os.path.join("data", "transactions.json")

def list_transactions():
    if not os.path.exists(DATA_PATH):
        print("Henüz kayıtlı bir işlem bulunmamaktadır.")
        return

    with open(DATA_PATH, "r") as f:
        data = json.load(f)

    if not data:
        print("Kayıtlı işlem bulunmamaktadır.")
        return

    print("\n📋 Tüm İşlemler:")
    print("-" * 40)
    for i, item in enumerate(data, 1):
        print(f"{i}. [{item['type'].upper()}] {item['amount']}₺ - {item.get('category', item.get('source', ''))}")
        print(f"   Not: {item['note']}")
        print(f"   Tarih: {item['date']}")
        print("-" * 40)
