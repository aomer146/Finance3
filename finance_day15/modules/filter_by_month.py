import json
import os
from datetime import datetime

DATA_PATH = os.path.join("data", "transactions.json")

def filter_by_month(month_number):
    if not os.path.exists(DATA_PATH):
        print("📁 Veri dosyası bulunamadı.")
        return

    with open(DATA_PATH, "r") as f:
        transactions = json.load(f)

    found = False
    for t in transactions:
        try:
            t_month = datetime.strptime(t["date"], "%Y-%m-%d %H:%M:%S").month
            if t_month == month_number:
                found = True
                print(f"[{t['type'].upper()}] {t['amount']}₺ - {t.get('source', t.get('category', ''))} - {t['note']} - {t['date']}")
        except Exception:
            continue

    if not found:
        print("🔍 Belirtilen aya ait kayıt bulunamadı.")
