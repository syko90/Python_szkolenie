'''
Python jest teraz bardzo popularnym językiem jeżeli chodzi analizę danych (matrix)
To jeszcze nie będzie tutorial związany z magicznym dizedziną Machine Learning
ale pokażę podstawową zintegrowana bibliotekę umozliwiającą statystyczną analize danych
Co tutaj możemy wyliczyć? średnią, medianę, modę, odchylenie standardowe, wariancję
'''

import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

x = statistics.mean(example_list)
print('średnia',x)

y = statistics.median(example_list)
print('mediana',y)

z = statistics.mode(example_list)
print('moda',z)

a = statistics.stdev(example_list)
print('dichylenie standardowe',a)

b = statistics.variance(example_list)
print('variancja',b)
