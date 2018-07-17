'''
W dzisiejszym odcinku powiemy sobie coś więcej o module
SYS, mamy tutaj funckje takie jak stdin(), stdout(), stderr()
sys.argv(). Ogólnie ten moduł daje nam możliwość zrobienia
takiego pomostu miedzy Python'em a innymi językami
'''

# funckja stdout, stdin możemy przekazywać wiadomości
# oraz błędy porzez cmd albo używać do logowania

# tutaj mamy przykład

import sys

print (sys.platform)

print (sys.version)

print(sys.path)

# wyświetl tylko 3 litery Twojego systemu
if sys.platform[:3] == 'win':
    print('Witaj uzytkowniku Windowsa')

if not sys.platform[:3] == 'mac':
    print('Hej, pracujemy na Windowsie a nie na Macu!')
