import sqlite3

conn = sqlite3.connect('./ch16/practice/books.db')
curs = conn.cursor()

ins = 'SELECT title FROM book ORDER BY title ASC'
for row in conn.execute(ins):
    print(row)