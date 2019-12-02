#funkcja zwraca liczbę kolejną liczbę pierwszą względem zadanej wartości
#piąta z kolei liczba pierwsza n=5 szukamy od zera
from datetime import date


def getPrimaryNumbers(n=5):
    primaryNumbers = [1]
    number=2
    while(len(primaryNumbers) <n):
        isPrimary=True
        for div in range(2,number):
           if(number %  div==0): #sprawdzenie podzielności
                isPrimary=False
        if(isPrimary):
            primaryNumbers.append(number)
        number +=1
    return primaryNumbers,primaryNumbers[len(primaryNumbers)-1]

#wywołanie funkci
element = 11
print("Lista: ",getPrimaryNumbers(element))
print("n-ty element: ",getPrimaryNumbers(element)[1])


def printParameters(login,password, email, status=True, registrationDate=date.today()):
    return("%s %s %s %s %s" % (login,password,email, status, registrationDate))

#różne wywołania
print(printParameters("rk","rk","rk"))
print(printParameters("rk1","rk1","rk1",registrationDate= "2020-01-01"))
print(printParameters("rk2","rk2","rk2",registrationDate= "2020-01-01", status=False))

def nonDefinedParameter(*elements):
    sum=0
    for elem in elements:
        sum+=elem
    return sum/len(elements)

print(nonDefinedParameter(1))
print(nonDefinedParameter(5,4,6))
print(nonDefinedParameter(2,2,2,2))

def sortList(numbers):
    numbers.sort()
    return numbers
list=[3,2,5,4,6]
print(sortList(list))

def bubblesort(elements, asc=True):
    noProbes=1

    #pętla iterująca po kolejnych próbach sortowania
    for probe in range(len(elements)-1): # determinujemy 5 prób w przypadku najgorszym
        isSorted = True
        for index,value in enumerate(elements):
            if(index == (len(elements)-1)):
                break
            if((elements[index]>elements[index+1]and asc)): # porównanie sąsiednich komórek
                isSorted=False
                elem=elements[index+1]              # wydobcie elementu na indeksie i+1 do zmienej
                elements[index+1]=elements[index]   # zamiana kolejności
                elements[index] = elem
            if((elements[index]<elements[index+1]and not asc)): # porównanie sąsiednich komórek
                isSorted=False
                elem=elements[index+1]              # wydobcie elementu na indeksie i+1 do zmienej
                elements[index+1]=elements[index]   # zamiana kolejności
                elements[index] = elem
        #print(noProbes,elements)
        if (isSorted):
            break
        noProbes+=1
    return elements
print(bubblesort([1,3,2,5,4,6]))

print(bubblesort([34,45,1,3,87,56,9],asc=True))
from datetime import datetime

t_start=datetime.now().microsecond/1000
print(bubblesort([3,2,1,5,4,6,21,34,44,22,20,55,4,1,55,66,2,4,1,1,54,3,11],asc=False))
t_stop = datetime.now().microsecond/1000
print(t_start)
print(t_stop)
print("czas wykonania funkcji w ms:",t_stop-t_start)


