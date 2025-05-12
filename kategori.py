from db import get_connection

def kategori_ekle(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def kategorileri_getir():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    kategoriler = cursor.fetchall()
    conn.close()
    return kategoriler
