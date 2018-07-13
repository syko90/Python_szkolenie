'''
czym jest plik .csv? Jes to plik gdzie mamy dane odzielone przecinkami
delimeter - takie określenie tutaj spotkacie to jest ogranicznik
'''

import csv

with open('plik.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
         print(row)
         print(row[0])
         print(row[0],row[1],row[2],)
