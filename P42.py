from random import sample
#losuje bez zwracania z populacji - listy wartosći
#określoną w argumencie metodą ile razy


liczby=range(1,50)
ile=6
wynik=sample(liczby,ile)
print(wynik)
wynik.sort()
print(wynik)
wynik.sort(reverse=True)
print(wynik)