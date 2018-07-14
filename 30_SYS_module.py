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

sys.stderr.write('To jest stderr text \n')
sys.stderr.flush()
sys.stdout.write('To jest stddout text \n')
