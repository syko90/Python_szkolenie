'''
W poprzednim odcinku korzystałem z takiego modułu statistics i użyłem takiego
słowa jak import
POKAZAĆ GDZIE ZNAJDUJĄ SIĘ BIBLIOTEKI
importując taki moduł myśl o nim jak zwykłym skrypcie, umieszczanie kodu w takich
modułach pozwala na organizację Twojego kodu w prosty sposób. Niektórzy piszą wszystko
w jednym skrypcie, inni preferują i w sumie ja też importowanie wielu modułów.
'''
# pokazać gdzie na dysku znajdują się moduły - i zobaczyć wnętrze modułu

# jak zaimportować moduł?

import statistics
''' w ten sposób załadowaliśmy moduł do pamięci
w ten sposób mamy dostęp wszystkich funkcji dostępnych w tym module
'''
# Jak teraz skorzystać z funkcji zawartych w tym module?

import statistics
lista = [1,5,2,6,4,2,6,5,4,52,1,5,2,5,6,1]
print(statistics.mean(lista))
# wow moduł liczy na średnią z liczb zawartych w liście!
# to jest podstawowy sposób importowania modułów, ale istnieje wiele więcej

# dobra, to teraz kolejny sposób

import statistics as s # teraz cały moduł ukryty jest pod literą {
print(s.mean(lista))

# możesz importować tylko niektóre funkcje z danego moduły, żeby nie zapychać pamięci
from statistics import mean
print(mean(lista))

# i teraz użyć odpowiedniego skrótu
from statistics import mean as m
print(m(lista))

# mozemy importować kilka funkcji
from statistics import mean as m, median as d
print(m(lista))
print(d(lista))

# możemy zaimportować także wszsytkie funkcje z danego modułu i wedy wywołując
# poszczególne funkcje nie trzeba wpisywać nazwy biblikoteki

from statistics import *
print(mean(lista))
print(variance(lista))
