import csv
import sqlite3

conn = sqlite3.connect('./ch16/practice/books.db')
curs = conn.cursor()

ins = 'INSERT INTO book VALUES(?, ?, ?)'
with open('./ch16/practice/books2.csv', 'rt') as f:
    books = csv.DictReader(f)
    for book in books:
        curs.execute(ins, (book['title'], book['author'], book['year']))

conn.commit()