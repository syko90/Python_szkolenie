'''
Tym razem zajmiemy się tym jak importowac pewne moduły, które pomogą nam w pisaniu
naszych programów, w poprzednim filmiku użyłem takiego słowa kluczowego import
i modułu Statistics. Słcuhaj te moduły są już instalowane razem z Pythonem i możesz
je znaleść u Ciebie na dysku. Ba! Możesz nawet takie moduły otworzyć i sprawdzić co znajduje
się w środku danego modułu (wyszukać w starcie i znaleść plik statistics.py)
Można też taki skrypt przeszukiwać CNTRL + F i wtedy można szukać
'''

# Przejdźmy teraz jak w praktyce takimi modułami się posługiwać
# Podstawowa opcja importu
lista = [1,5,2,1,3,6,4,5,8,5,48,9,22,63,154,5]

'''
import statistics

print(statistics.mean(lista))
'''

# importowanie biblioteki z pomocniczą literką
# teraz można korzystac z całego modułu uzywając skrótu!
'''
import statistics as s

print(s.mean(lista))
'''

from statistics import mean
# w tym momencie zaimportowaliśmy tylko moduł mean z tej biblioteki
print(mean(lista))

# oczywiście teraz też możemy wykorzystać skrót
from statistics import mean as m
print(m(lista))


# możemy także zaimportować kilka modułów
from statistics import mean as m, median as d
print(m(lista))
print(d(lista))

# Ok, a co jeśli chcemy ziamportowac wszystkie funkcje z danej biblioteki, ale
# nie chcemy za każdym razem wpisywac słowa statistics tylko korzystać odrazu z w
# wewnętrznych funkcji. o może Cieie przyspieszyć jak masz grube palce.

from statistics import *

print(mean(lista))







