import csv

with open('./ch16/practice/books1.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(books)