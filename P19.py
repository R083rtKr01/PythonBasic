name = input("Podaj imię: ")  # input zwraca string
lastname = input("Podaj nazwisko: ")
age = input("Podaj wiek ")
position = input("Podaj stanowisko: ")
salaryNet = float(input("Wprowadź wynagrodzenie"))  # konwersja string na float
print("Pan/i", name, lastname,"(", age, "lat) pracuje na stanowisku",position,"(pensja:" , str(salaryNet * 1.23), "zł)")



birthdate = input("Podaj datę urodzenia (YYYY-MM-DD): ")
print ("Wiek:"+ str(2019 - int (birthdate[0:4])))

