#ćwiczenie 39
WordToNums={}
WordToNums["jeden"] = 1
WordToNums["dwa"] = 2
WordToNums["trzy"] = 3
WordToNums["cztery"] = 4
WordToNums["pięć"] = 5
wybrany=input("Podaj cyfre słownie z zakresu (1-5)").lower()
#print(WordToNums.values())
#print(WordToNums.keys())
#print(WordToNums[])

#drugie rozwiązanie

if(wybrany in WordToNums):
    print(WordToNums[wybrany])
else:
    print("Podałeś zły numer")

