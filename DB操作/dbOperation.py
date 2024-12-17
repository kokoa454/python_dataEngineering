import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

yesORno = True

while(yesORno == True):
    print("ユーザーを追加しますか?")

    if input("yes/no: ") == "yes":
        id = input("ID: ")
        name = input("名前: ")
        age = input("年齢: ")

        cursor.execute("INSERT INTO users (id, name, age) VALUES (?, ?, ?)", (id, name, age))

        print("ユーザーを追加しました")
    else:
        yesORno = False

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("データ一覧: ")
for row in rows:
    print(row)

conn.commit()
conn.close()