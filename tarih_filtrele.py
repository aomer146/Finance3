from db import get_connection

def islemleri_tarihe_gore_getir(start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.id, u.username, c.name AS category, t.amount, t.date, t.description
        FROM transactions t
        JOIN users u ON t.user_id = u.id
        JOIN categories c ON t.category_id = c.id
        WHERE date(t.date) BETWEEN date(?) AND date(?)
        ORDER BY t.date
    """, (start_date, end_date))
    results = cursor.fetchall()
    conn.close()
    return results
