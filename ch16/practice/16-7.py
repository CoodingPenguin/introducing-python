import sqlite3

conn = sqlite3.connect('./ch16/practice/books.db')
curs = conn.cursor()
ins = 'SELECT * FROM book ORDER BY year'

for row in conn.execute(ins):
    print(row)