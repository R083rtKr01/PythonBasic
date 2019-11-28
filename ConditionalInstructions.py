from datetime import date

#today=date.today()
#birthDate=input("Wprwoadz date urodzenia w formacie YYYY-MM-DD")
#year = birthdayDate[:4]
#if(year.isdecimal()):


### dokończyć bo się komp zrestartował


# za pomocą wyrażenia 3argumentowego sprawdz czy wprowadzona wartośc z klawiatry jest liczbą
# jeżeli tak to wypisz tą liczbę
#jezeli nie wypisz zero

Wartosc=input("podaj liczbę")
valnum = int(Wartosc) if Wartosc.isdecimal() else 0
print("wynik: ", valnum)
