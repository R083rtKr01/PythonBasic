#elements=[1,2,3,4,5,6,7]
elements=range(5,50,1)
index =0
#while(True):
while(index<len(elements)):
    print(index,elements[index])
    index += 1                    #inkrementacja indeksu
    if(index == len(elements)-1): # warunek przerwania
        break;                    # przerwanie

# wprowadź dane z klawiatury tak długo aż użytkownik wpisze Q
elements=[]
flag=True
while(True):
    elem=input("wpisz wartośc lub wprowadź Q żeby zakończyć")
    if(elem.upper()=="Q"):
        print("wyjście")
        flag=not flag
        break
    elements.append(elem)
else:
    print(elements)

