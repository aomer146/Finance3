import sqlite3

# Veritabanına bağlan
conn = sqlite3.connect('veritabani.db')  # Burada 'veritabani.db' dosyasının tam yolunu kullanabilirsin

# Cursor oluştur
cursor = conn.cursor()

# Tablo isimlerini almak için sorgu çalıştır
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Sorgu sonucunu al
tables = cursor.fetchall()

# Tablo isimlerini yazdır
for table in tables:
    print(table)

# Bağlantıyı kapat
conn.close()
