import json
import os
from datetime import datetime

DATA_PATH = os.path.join("data/transactions.json")

def filter_by_date(start_date_str, end_date_str):
    if not os.path.exists(DATA_PATH):
        print("📁 Veri dosyası bulunamadı.")
        return

    try:
        start = datetime.strptime(start_date_str, "%Y-%m-%d")
        end = datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        print("❌ Tarih formatı geçersiz. (Doğru format: YYYY-MM-DD)")
        return

    with open(DATA_PATH, "r") as f:
        transactions = json.load(f)

    found = False
    for t in transactions:
        try:
            t_date = datetime.strptime(t["date"][:10], "%Y-%m-%d")
            if start <= t_date <= end:
                found = True
                print(f"[{t['type'].upper()}] {t['amount']}₺ - {t.get('source', t.get('category', ''))} - {t['note']} - {t['date']}")
        except ValueError:
            continue

    if not found:
        print("🔍 Belirtilen tarih aralığında kayıt bulunamadı.")
