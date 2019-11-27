kwota = float(input("podaj kwotę brutto:"))
vat3 = 0.03
vat8 = 0.08
vat23 = 0.23

print(round (kwota,2)," zł brutto da nam ", round(kwota/(1+vat3),2)," zł netto", "przy vat =",vat3)
print(round (kwota,2)," zł brutto da nam ", round(kwota/(1+vat8),2)," zł netto", "przy vat =", vat8)
print(round (kwota,2)," zł brutto da nam ", round(kwota/(1+vat23),2)," zł netto", "przy vat =",vat23)



