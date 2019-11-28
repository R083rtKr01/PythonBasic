sentence = "Ala ma kota, kot ma Ale."
# oczyścic ze znaków interpunkcyjnych

sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")
print(sentence)

# zapisz wszystkie słowa w zdaniu w liście words
words = sentence.split(" ")
print(words)

# listy
params = []
row = [1, "Adam", "Nowak", "2000-01-01", True, 5500.]

# dodawanie parametrów do parms

params.append(12.5)
params.append(11.5)
params.append(9.4)

# wypisanie elemntów listy

# print(params)
# print(row)

# zmiana pensji w liście row

row[5] = 6000.
print(row)
# odczyt elementów z krokiem 2
print(row[0:5:2])  # wskazanie kolejności prezentacji indeksów
print(row[1:])  # pokazanie od którego do końca mają byc prezentowane indeksy
print(row[:3])  # wyswietlenie pierwszych 3 indeksów
print(row[::-1])  # odwrotna kolejność
# powielanie list
row = row * 2
print(row)
# row *= 0 # row =row*0 kasuje nam liste
# print(row)

# długośćlisty

print(len(row))

# row[1] = "abc" gdybym tak zadał a row jest puste to otrzymam błąd

row[6:] = [2, "Jan", "Kowalski", "2011-02-12", False, 10000]
print(row)

a = ["a", 1, True]
b = [False, "xyz", 15.3]
# print(a[0]>b[0]) # jak porównywać sublisty na konkretnych indeksach

print("Kowalski" in row)
print("Kowalski" not in row)

name = "Robert"
# konwersja na listę
name = list(name)
name[3] = 'k'
print(name)

string = ""
for v in name:
    string += str(v);
print(string)  # z wcięciem robi się po kolei

print(name)
name = str(name)
name = name.replace("'", "")
name = name.replace(", ", "")
name = name.replace("]", "")
name = name.replace("[", "")
print(name)

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)  # lub numbers.remove(numbers[3]) pierwsza opcj jest usuwaniem wartości a ta zakomentowana do indeksów
print(numbers)
deleted = numbers.pop(2)  # usuwanie wartości po indeksie
print(numbers)
print(deleted)

# sprawdzić czy dwa napisy sa palindromami (inna wersja czy liczby są lustrzane)

text = "kajak"
# I sposób
print(text[:] == text[::-1])

# II sposób
text = list(text)
textRev = text
textRev.reverse()
print(text == textRev)

# sortowanie
nums = [1.1,2.1,0.15,15.,1.,4.,1]
nums.sort()
print(nums)
nums.sort(reverse=True)

names = ["Ala","Ola","Ela"]
names.sort() # trzeba najpierw posortować bo printem nie możemy zlecić i pokazać posortowane
print(names)

kik =[
    ["-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-","-"]
]
print(kik)
print("lista zewnętrzna",len(kik))
print("pierwszy wiersz",len(kik[0]))
print("drugi wiersz",len(kik[1]))
print("trzeci wiersz",len(kik[2]))

kik[2][3] = "X"
kik[1][1:3] = ["O","O"]
print(kik)
kik.append(["*","*","*"])
print(kik)

# kik = ["*","*","*"]+kik
kik.insert(0,["*","*","*"])
print(kik, len(kik))


#krotka

#krotka może zawierać w sobie edytowalne elementy

tupleType=(1,2,3)
# tupleType[1] = 55 # krotka jest typem NIEZMIENNYM
print(tupleType)

#ALE

multiDimTuple=(a,[3,4],[5,6])
a=[1,2]
#multiDimTuple[0] = 1

multiDimTuple[0].append('X')
multiDimTuple[0][0]=2
print(multiDimTuple)

print(id(a))
print(id(multiDimTuple[0]))


#Słowniki

products = {}

#dodanie nowego produktu

products["0x111"] = "Pamięć RAM 8GB"
products["0x112"] = "Pamięć RAM 16GB"
products["0x222"] =[1,"PC","Intel i5 8gen",700]

#modyfikacja pamięci RAM
products["0x112"] += " NEW"
products[None] = "xxx"
print(products[None])
print(products)
print(products.keys())
print(products.values())

#zbiory

A = set([1,2,3,4,5,6])
B = set([4,5,6,7,8])

print("suma A i B", A|B)
print("część wspólna A i B",A&B)
print("różnica A-B", A-B)
print("różnica B-A", B-A)
print("różnica symetryczna dla A i B", B^A)

#dla zdania wprowadzonego przez użytkownika sprwdz ile jest unikatowych słów

zdanie=input("podaj zdanie")
slowa=zdanie.split(" ")
unikaty=set(slowa)
print(unikaty, "liczba słów w zbiorze", len(unikaty),
      " oraz liczba powtórzeń pewnego słowa w zbiorze wynosi", len(slowa)-len(unikaty))

S=set([1,2,3])
L=['a','a','A']
D={'a':11,'b':11,'c':1}
print(s)
print(list(s))
print(set())