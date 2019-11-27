# V=SPK*(1+p/m)**(n*m)

SPK=float(input("podaj kwotę początkową: "))
p =int(input("podaj oprocentowanie"))/100
n=int(input("podaj czas trwania lokaty"))
m=int(input("podaj liczbę okresów kapitalizacji w roku"))

print(round(SPK*(1+p/m)**(n*m),2))