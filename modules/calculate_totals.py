import json
import os

DATA_PATH = os.path.join("data/transactions.json")

def calculate_totals():
    if not os.path.exists(DATA_PATH):
        print("Henüz hiç işlem yok.")
        return
    with open(DATA_PATH, "r") as f:
        transactions = json.load(f)
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    print(f"📊 Toplam Gelir: {total_income}₺")
    print(f"📉 Toplam Gider: {total_expense}₺")
    print(f"💰 Net Bakiye: {total_income - total_expense}₺")
