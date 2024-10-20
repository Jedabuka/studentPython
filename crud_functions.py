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
    price INTEGER NOT NULL)
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    ''')


initiate_db()

def add_product(*args):
    cursor.execute('INSERT OR IGNORE INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (f'{args[0]}', f'{args[1]}', f'{args[2]}'))
    conn.commit()


for i in products:
    add_product(*i)

def add_user(username, email, age):
    with sqlite3.connect('products.db') as con:
        cur = con.cursor()
        cur.execute('INSERT OR IGNORE INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                    (f'{username}', f'{email}', f'{age}', 1000))

def is_included(username):
    with sqlite3.connect('products.db') as con:
        cur = con.cursor()
        check_user = cur.execute('SELECT * FROM Users WHERE username=?', (username,))
        if check_user.fetchone() is not None:
            return True

def get_all_products():
    with sqlite3.connect('products.db') as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Products ORDER BY id ASC')
        rows = cur.fetchall()
        return rows


conn.commit()
conn.close()
