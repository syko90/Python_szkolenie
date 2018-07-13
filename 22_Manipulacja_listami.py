# jak manipulowac listami
# jak dodawać elementy, usuwać, doklejać, sortować itd.

# didajmy prosta listę

x = [1,6,3,2,6,1,2,6,7]
# dodajmy jakiś element do listy

x.append(55)
print(x)

# dodajmy cos w środku listy
x.insert(2,33)
print(x)

# możemy też wyrzucać pewne elementy z listy
x.remove(6)
print(x)

# oczywiście możemy dostać się do określonego elementu listy
print(x[5])

# możemy też wyszukać element po indeksie
print(x.index(1))

# zliczamy elementy listy
print(x.count(1))

# co jeszcze? np sortowanie listy
x.sort()
print(x)

# super a co jeśli mamy listę pełna napisów czyli stringów?
y = ['Jan', 'Maciej', 'Ewelina', 'Gosia']
y.sort()
print(y)
y.reverse()
print(y)
