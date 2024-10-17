import sqlite3


conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(1, 11):
    cursor.execute('INSERT OR IGNORE INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                    (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))

for i in range(1, 11, 2):
    cursor.execute(f'UPDATE Users SET balance = ? WHERE username = ?', ('500', f'User{i}'))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))

cursor.execute(f'SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()

for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]}, Баланс: {user[3]}')

cursor.execute('DELETE FROM Users WHERE id = ? or username = ?', (6, 'User6'))

cursor.execute('SELECT COUNT(*) FROM Users')
all_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_sum_balance = cursor.fetchone()[0]
print(all_sum_balance / all_users)

conn.commit()
conn.close()
