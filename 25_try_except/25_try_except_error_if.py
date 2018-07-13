'''
słowa try możemy postawić przed jakimkolwiek kawałkiem kodu
to jest coś takiego jak blok if ale działa dla całego bloku kodu
jak to wygląda w praktyce?
'''
# tutaj mamy kawałek kodu z porzedniego tutorialu

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


try:
    JakiKolor = input('Dla jakiego koloru chcesz pobrać datę?')

    if JakiKolor in kolory:
        KolorIndex = kolory.index(JakiKolor)
        iData = daty[KolorIndex]
        print('Data ',JakiKolor,'to',iData)
    else:
        # zamiast łapać wszystkie błedy w całym bloku zrobimy to na warunku if
        print('Ten kolor nie został znaleziony.')

except Exception as e:
    print(e)
