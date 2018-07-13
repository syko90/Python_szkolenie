'''
czym jest plik .csv? Jes to plik gdzie mamy dane odzielone przecinkami
delimeter - takie określenie tutaj spotkacie to jest ogranicznik
'''

import csv

with open('plik.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    daty = []
    kolory = []
    for wiersz in readCSV:
        kolor = wiersz[3]
        data = wiersz[0]

        daty.append(data)
        kolory.append(kolor)

    print(daty)
    print(kolory)

    JakiKolor = input('Jaki kolor szukasz?')
    KolorIndex = kolory.index(JakiKolor)
    iData = daty[KolorIndex]
    print('Twój kolor, którego szukasz to: ', JakiKolor,' ,a to jest jego data', iData)
