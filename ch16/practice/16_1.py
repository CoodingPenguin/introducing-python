import csv

books = [
    ['author', 'book'],
    ['J R R Tolkien', 'The Hobbit'],
    ['Lynne Truss', 'Eats, Shoots & Leaves']
]

with open('./ch16/practice/books1.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(books)