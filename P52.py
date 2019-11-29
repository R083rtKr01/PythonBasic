#tabliczka mnożenia dla zadanego zakresu wartość końcową przedziału pomniejsza się o 1 bo indeksy zaczynają się od 0
x= range(1,16)
for i in x:
    for j in x:
        print("%3i"% (i*j), end=" ")
    print()