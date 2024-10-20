import sqlite3


conn = sqlite3.connect('products.db')
cursor = conn.cursor()

products = [
    ['Персик', 'Сочный фрукт с бархатистой кожицей', 100],
    ['Гранат', 'Отличная замена попкорну', 200],
    ['Манго', 'Райское наслаждение', 300],
    ['Ананас', 'Спелый! Ваш рот останется цел', 400]
    ]

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')


initiate_db()

def add_product(*args):
    cursor.execute('INSERT OR IGNORE INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (f'{args[0]}', f'{args[1]}', f'{args[2]}'))


for i in products:
    add_product(*i)


def get_all_products():
    with sqlite3.connect('products.db') as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Products ORDER BY id ASC')
        rows = cur.fetchall()
        return rows


conn.commit()
conn.close()
