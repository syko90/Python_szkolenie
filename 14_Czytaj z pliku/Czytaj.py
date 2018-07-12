# Czytanie z pliku Python szkolenie
'''
 Wiemy juz jak zapisywac do pliku oraz jak dołączać dane do pliku, ale chcemy
także wiedzieć jak odczytywać dane z pliku i używac ich w naszych programach
Python. Jest to bradzo prosta operacja i ma podpobną składnięd o wcześniejszych operacji
'''

# tutaj literka 'r' służy do czytania, napisz coś takeigo i juz możesz czytać

#czytaj = open('przykład.txt','r').read()
#print(czytaj)

# czasami ludzie czytają pliki z wieloma linimi. Może być to np lista nazwisk
# albo coś w tym stylu. Możemy wtedy użyc polecenia .readline() co umożliwia
# wrzucenie wszystkiego w liste Pythonowską

czytaj1 = open('przykład.txt','r').readlines()
print(czytaj1)
