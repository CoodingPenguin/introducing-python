import sqlite3

conn = sqlite3.connect('./ch16/practice/books.db')
curs = conn.cursor()
curs.execute('''
    CREATE TABLE book (title TEXT, author TEXT, year INT)
''')
conn.commit()