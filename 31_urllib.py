'''
Biblioteka urlib - daje nam niesamowite możliwości, bo otwiera nam drzwi
do internetu. Dzięki tej bibliotece możesz dostać się do stron, pobierać dane,
parsować dane i robić zapytania GET oraz POST ( czyli coś w stulu wyślij/pobierz)

Niektóre strony internetowe jednak nie dają Ci pozwolenia do danyhc znajdujących się
na ich serwerach. Jeżeli serwer odrkryje, że jest odpytywane przez jakis program
może czasami Ciebie zablokować albo wypluć Ci dane inne niż normalny uzytkownić
może zobaczyć. To może być czasami irytujące na początku, ale możemy to ominąć
pisząc prosty kod.

Aby to zrobić, wystarczy zmodyfikować program użytkownika, który jest zmienną
w nagłówku, który wysyłasz. Nagłówki to fragmenty danych udostępniane serwerom,
aby poinformować je o tobie. Tutaj domyślnie Python informuje stronę, którą
odwiedzasz za pomocą urllib Pythona i wersji Pythona. Możemy jednak to
zmodyfikować i zachowywać się tak, jakbyśmy byli użytkownikiem
Internet Explorera, użytkownikiem Chrome lub cokolwiek innego!

Czasami stronka może udostępniać Ci dostęp do takeigo czegoś jak API(Application
Intereface) i właśnie ten interfejs jest przeznaczony specjalnie do udostępniania
programom pisanym przez programistów.
Nasze programy są w sumie zainteresowane tylko danymi a nie kodami HTML danej stronyself.
'''

# Teraz zrobimy proste zapytanie
import urllib.request

x  = urllib.request.urlopen('http://www.wago.pl')
print(x.read())

'''
Tutaj pojawia się pojęcia używania wyrażeń regularnych, żeby oczyścić te śmieći,
które dostaliśmy.
