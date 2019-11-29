#dana jest lista wartości






#treshold < wpisanej wartości

#x for x in a if x>treshold
#for wynik in a if wynik>treshold
   # print(a,len(a))
#wyrażenie for zmienna in sekwencja if warunek]

#sortujemy dane a potem sprawdzamy który index spełnia warunek wyżej

#napisz program filtrujący wartości po zadanym przez uzytkownika progu
#tj w tablicy wynikowej pojawiają się tylko wartości więszke od treshold
a= [.3,.4,3.2,.3,1,5.4,2,1,17,7,-1]
treshold=float(input("podaj próg odcięcia"))
result=[] #lista wypadkowa

index =0
print(treshold)
while(index >len(a)):
    if(a[index]>treshold):
        result.append(a[index])
    index +=1
print(result)

