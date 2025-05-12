from db import get_connection

def islem_ekle(user_id, category_id, amount, date, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (user_id, category_id, amount, date, description)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, category_id, amount, date, description))
    conn.commit()
    conn.close()

def islemleri_getir():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.id, u.username, c.name AS category, t.amount, t.date, t.description
        FROM transactions t
        JOIN users u ON t.user_id = u.id
        JOIN categories c ON t.category_id = c.id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows
