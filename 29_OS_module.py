'''
Najważniejszą cechą modułu OS jest interakcja z Twoim
systemem operacyjnym. Co możesz z tym robić? tworzyć foldery
przenosić foldery i czasami zmieniać ścięzkę w której
pracujesz. Możesz także mieć dostęp do nazw plików wykorzystując
funkcję listdir().
'''

# przykłady
import os

# wyświetl daną ścieżkę
curDir = os.getcwd()
print('To jest Twoja ścieżka ',curDir)

# utwórz nową lokalizację/ pom prostu utwórz folder
os.mkdir('nowaLokalizacja')

# żeby zmienić nazwę lokalizacji należy
os.rename('nowaLokalizacja','nowaLok')

#  usuń lokalizację/fodler
os.rmdir('nowaLok')
