import json
import os
from datetime import datetime

DATA_PATH = os.path.join("data/transactions.json")

def add_expense(amount, category, note=""):
    transaction = {
        "type": "expense",
        "amount": amount,
        "category": category,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump([], f)
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    data.append(transaction)
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)
    print("✅ Gider eklendi.")
