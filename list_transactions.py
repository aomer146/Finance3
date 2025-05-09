import json
import os

DATA_PATH = os.path.join("data", "transactions.json")

def list_transactions():
    if not os.path.exists(DATA_PATH):
        print("Henüz hiç işlem yok.")
        return

    with open(DATA_PATH, "r") as f:
        transactions = json.load(f)

    if not transactions:
        print("Henüz hiç işlem yok.")
        return

    for i, t in enumerate(transactions, 1):
        print(f"{i}. [{t['type']}] {t['amount']}₺ - {t.get('source', t.get('category', ''))} - {t['note']} - {t['date']}")
