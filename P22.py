
salaryNet = float(input("Wprowadź wynagrodzenie netto "))
godziny = float(input("podaj liczbę godzin "))
vat23=0.23

print("stawki wynoszą odpowiednio:",round(float(salaryNet * (1+vat23)/godziny),2), "zł/h brutto oraz",round(salaryNet/godziny,2),"zł/h netto")
