# ctrl +/ -> komentarz
'''

komentarz blokowy
'''

print("witaj w pythonie")

# WSZYSTKO co jest w pythonie jest obiektowe


# ZMIENNE

# w pythonie można dawać w '' lub "" ale praktya jest taka ze zmiene znakowe zapisuje się w apostrofach np 'a'
# a wielo znakowe "twój stary"
# w pythonie nie ma deklaracji zmiennych. jest deklaracja i przypisanie -> inicjalizacja zmiennej (obiektu)

text = "witaj"
name = "Robert"
sign = 'a'
print(text + " " + name)
# zasady nazewnictwa: z dobrych praktyk nie uzywamy polskich znaków
# uwaga na duze znaki - zmienne napisane małymi literami są odrózniane od tych pisanych duzymi
# nie ma spacja w nazwach zmienych
# wystrzegamy sie nazw zastrzeżonych
# cyfry nie mogą rozpocyznac nazwy zmiennych

# zmienne a pdstawie innych zmiennych
a = 1
b = a + 1
print(a, b, (a * b), )

# ctr + d to duplikowanie lini jak w workbenchu
print(a, end=';')
print(b, end=';')
print(a + b, end='\n')  # \n new line
print('www.xyz.pl\\all')  # \\ daje nam jeden backslash
print('www.xyz.pl\\\\all')  # \\ daje nam jeden backslash
print('"cytat"')
print("\"Cytat\"")
print("I'm Robert")
# kasowanie zmiennej usuwanie obiektu z Pamięci podręcznej
# del (nazwa zmiennej)
# del(a)
# print(a)

# zwraca NameError: name 'a' is not defined

# podstawowa instrukcja to PRINT

# ćwiczenie 1
# wprowadz zmienne a b i c o wartosciach 1, 2.4 i w1 oddziel je tabulatorami \t
a = 1
b = 2.4
c = "w1"
print(a, b, c, sep='\t\t')
# sep= definiuje separator

# ćwiczenie p2

a = 2.1
b = "abc"
c = 0
print(a, b, c)

# ćwiczenie p3

a = 13
b = c
c = 0
print(a, b, c)

# ćwiczenie p4
# del (a)
# del (c)

c = c + 31.3
print(c)

# operacje na liczbahc
num1 = 1
num2 = 2

print(type(num1), type(num2), 1 / 2)
print(type(num1), type(num2), 1 // 2)

# konwersja rozszerzajaca i zawęzajaca
print(int(111.9999999))

floatNum = 111.99999999
floatNum = int(floatNum) #konwersja zaweżająca
print(floatNum)
intNum=5
print(float(intNum)) #konwersja rozszerzająca

# Warto zapamietac!!! zasady matematyczne nie mają znaczenia

# typ logiczny

print(bool(121),bool(0))
print(bool("dead"),bool(""))
print (bool(12.2),bool (0.))


#string

name = "Robert"
print("długość to: ",len(name))
print(name[0])
print(name[len(name)-1])

name = name +" "+"Król"
print("ADD: "+ name)
name = name[0:6] #to oznacza ze pokazujemy znaki od pierwszego (liczymy od zera) do 6 ale bez 6 znaku
print("SUB: " + name)

# # -*- coding: utf-8 -*- do wymuszenia kodowania UTF8

#konwersja na strin

#flag = True
#print(str(flag))
#print(int(flag))

x=1 # przypisanie do obiektu
result= (x == 1) # porównanie wartości przyjmowanej przez obiekt x z liczbą 1
print (x==1)
print (result)
# print((x=1) błąd

name1 ="ala"
name2 ="Ala"
print("==",name1==name2) # leksykograficznie duże litery są mniejsze od małych
print(">",name1>name2) # leksykograficznie duże litery są mniejsze od małych


