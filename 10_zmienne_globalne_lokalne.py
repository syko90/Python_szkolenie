x = 6

def test(modyfikuj):
   print(modyfikuj)
   modyfikuj += 20
   return  modyfikuj
      
y = test(x)
print('zmienna y',y)
