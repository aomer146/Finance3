# Muhasebe Uygulaması

Basit komut satırı tabanlı gelir/gider takip uygulaması.



## Kullanım

Menüdeki seçenekleri numara olarak girin:

1. **Gelir ekle**  
2. **Gider ekle**  
3. **Tüm işlemleri listele**  
4. **Toplam gelir ve giderleri göster**  
5. **Kategori/kaynak/not’a göre filtrele**  
6. **Tarih aralığına göre filtrele**  
7. **İşlem sil**  
8. **İşlem güncelle**  
9. **CSV olarak dışa aktar**

## Özellikler

- **Day 1**: Proje yapısı oluşturuldu  
- **Day 2**: `add_income.py`, `add_expense.py` modülleri eklendi  
- **Day 3**: `transactions.json` ile kalıcı veri  
- **Day 4**: `list_transactions.py` → Tüm işlemleri listeleme  
- **Day 5**: `calculate_totals.py` → Toplam gelir/gider hesaplama  
- **Day 6**: `filter_transactions.py` → Metin bazlı filtreleme  
- **Day 7**: `delete_transaction.py` → İşlem silme  
- **Day 8**: `filter_by_date.py` → Tarih aralığına göre filtreleme  
- **Day 9**: `update_transaction.py` → İşlem güncelleme  
- **Day 10**: `export_to_csv.py` → CSV dışa aktarma  
- **Day 11**: README güncellemesi

## Dosya Yapısı

```
finance_day11_complete/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── add_income.py
│   ├── add_expense.py
│   ├── list_transactions.py
│   ├── calculate_totals.py
│   ├── filter_transactions.py
│   ├── filter_by_date.py
│   ├── delete_transaction.py
│   ├── update_transaction.py
│   └── export_to_csv.py
└── data/
    ├── transactions.json
    └── transactions_export.csv  _(CSV dışa aktarım sonrası oluşturulur)_
```


