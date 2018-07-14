'''
Ok to dzisiaj powiemy sobie trochę więcej o wbudowanych funkcjach, cały opis
funkcji możesz znaleść na tej stronie: https://docs.python.org/3/library/functions.html
Lecimy z przykładami
'''
# wbudowane funkcje nie muszą być wcześniej importowane !!
Num1 = -10
Num2 = 10
print(abs(Num1))

if abs(Num1) == Num2:
    print('True!')

# wiele ludzie nie wie nawet, że taka funkcja istnieje
# jest to funckja help(), sprawdźmy
help()

# albo coś takiego
import time
help(time)

# lista i wartości MIN MAX
lista = [5,2,1,6,7]

najwiekszy  = max(lista)
print(najwiekszy)

najmniejszy = min(lista)
print(najmniejszy)

# zaokrąglanie
x = 5.622
x = round(x)
print(x)

y = 5.256
y = round(y)
print(y)

# konwersja typów danych
intTest = '55'
inTest = int(inTest)
print(inTest)

strNapis = 55
strNapis = str(strNapis)
print(strNapis)

rTest = 55
rTest = float(rTest)
print(strNapis)
