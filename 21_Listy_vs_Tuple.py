'''
Dzisiaj skupimy się nad róznica pomiędzy listami a tuplami(krotka) w Pythonie
Są między nimi podobiestwa, więc czasami sa mylone między sobą.
Tuple jest to element danych, oddzielony przecinkami i sa to tak zwane
elementy "immutable". To oznacza, że nie moga być zmieniane, modyfikowane.
Temat jest tego typu, że dzięki tej cesze Tuple znajdują zastosowanie w różnych
miejscach. Ttuaj mamy przykład
'''

def test():
    return 15, 12

x, y = test()
print(x, y)

# w tym wypadku funckja zwraca jakieś liczby i to są własnie Tuple
# nie chcemy wpływać na te wartości i o to chodzi

'''
zauważ, że tuple nie mają wokół siebie żadnych nawiasów etc. (czasami mogą być
naiwady ale tylko okrągłe)

Teraz przejdziemy do bardziej popularnych elementów w Python. Są to listy
Listy definiujemy w kwadratowych nawiasach. Listy są w sumie odpowiednikami
takich elementów jak tablice w innych językach programowania
'''
x = [1,3,5,6,2,1,6]

# możesz teraz odnieść się do calej listy np poniższą komendą

print(x)

# albo możesz odnieść się do pojedyczego elementu tablicy

print(x[0], x[1])
