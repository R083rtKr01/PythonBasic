# napisać program który na podstawie danych magazynowych i danych zamowienia klienta przygotuje paragon z kwotą

warehouse={"1":["A",3.5,10],
           "2":["B",2.99,5],
           "3":["C",9.99,1]}
print(warehouse)
dozaplaty=0
#koszyk zawiera listy zamówionych produktów
basket=[]
#CLI uzytkownika (comannd line interface)
while True:
    print("|%3s|%10s|%10s|%10s|"
          %("ID","NAZWA","CENA","ILOŚć"))
    for key in warehouse.keys():
        print("| %3s | %10s |%5.2f zł| %5.1f szt|"
              %(key,warehouse[key][0],warehouse[key][1],warehouse[key][2]))
    # pobieranie danych od uzytkownika
    choice = input("Podaj Id produktu który chcesz zamówić, Q - wyjście")
    # wyjście z programu
    if(choice.upper()=="Q"):
        print("Zamówienie złożone /Wyjście jeśli pusty")
        # print("twój koszyk: ", basket)
        print("suma do zapłaty", dozaplaty, " zł")
        break
    #sprawdzenie czy istnieje taki id
    if(choice not in warehouse.keys()):
        print(("nie ma takiego produktu"))
        continue

    while(True):
        try:
            quantity=float(input("Wprowadź ilość zamawianego produktu, krotność 1"))
        except:
            print("Błędny typ danych wprowadź liczbę")
            continue
        #sprawdzenie dostępności produktu

        if(quantity>warehouse[choice][2] and quantity >=0):
            print("niestety jest tylko: "+str(warehouse[choice][2])+ "szt")
            continue
        else:
            break

        #aktualizacja magazynu i koszyka
    warehouse[choice][2]-= quantity
    basket.append([warehouse[choice][0],warehouse[choice][1],quantity])
    #suma skumulowana zamówień w koszyku
    dozaplaty+=quantity*warehouse[choice][1]
    print("twój koszyk: ")
    for element in basket:
        print("|%10s|%8.2f zł|%5.1f|"
              % (element[0].center(10),element[1],element[2]))

    print("suma do zapłaty: %.2f zł" % dozaplaty,)


