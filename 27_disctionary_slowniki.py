'''
Najbardziej pożytczenym typem danych w Python sa dictionary czyli słowniki
Do zapamiętania mamy tutaj kilka pojęć. W Dictionary ważne jest pojecie key
i value. Wszystkie wartości key (słowa klucze?) są unikalne.
Dobra lecimy  z przykładem
'''

# Słownik imion ośób oraz odpowiadający im wiek

exDict = {'Maciek':15, 'Gienek':22,'Ziutek':12,'Max':17}

print(exDict)

# ile lat ma Maciek?
print(exDict['Maciek'])

# chcemy wstawić nową osobę do słownika

exDict['Tomek'] = 30
print(exDict)

# ale niestety Tomek szybko umarł, więc usuwamy go ze słownika
del exDict['Tomek']
print(exDict)

# no dobra to do naszego słownika dodajemy dla każdeej osoby kolor włosów

exDict = {'Maciek':[15,'blondyn'], 'Gienek':[22,'szatyn'],'Ziutek':[12,'rudy'],'Max':[17,'brunet']}
print(exDict['Gienek'][1])
