#ćwiczenie 41

products={}
id =1
#while(True):
while(id <=3):
     products[id] =[input("Podaj nazwę produktu "),
                   int(input("Podaj ilość ")),
                   float(input("Podaj cenę netto"))]
     id += 1
print(products)
