import csv

with open('books1.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

print(books)