# utworzyć listę wartości, mogą się powtarzać
# Napisz program, który znajdzie i wyświetli
# pozycję na liście pierwszego wystąpienia określonej liczby.


import random
listaRND=[]
for i in range(10):
    listaRND.append(random.randint(1,10))
print(listaRND)
#wyszukaj element z listy i zwróc jego indeks
# jezeli elementu nie a na liście to zwróć -1
find = int(input("podaj liczbę z zakresu od 1 do 10"))
# sprawdzamy czy element występuje w liście
if(find not in listaRND):
    print("Element %i nie występuje w liście"% find)
else:
    for index,value in enumerate(listaRND):
        if(value==find):
            print("Element %i znajduje się na indeksie %i"%(find,index))
            break

#ile razy występuje na liście
count=0
for element in listaRND:
    if(element==find):
        count+=1
print("Element %i występuje w liście %i razy"%(find,count))