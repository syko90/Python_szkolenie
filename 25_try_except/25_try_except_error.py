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
        JakiKolor = input('Jakiego koloru chcesz pobrać datę?')
        KolorIndex = kolory.index(JakiKolor)
        iData = daty[KolorIndex]
        print('Data koloru',whatColor,'to:',theDate)


    except Exception as e:
        print(e)


    ''' Jeżeli w bloku try zostanie wykryty błąd to zostanie wykonany blok
    exception
    '''
    print('To jest wykonywane!')
