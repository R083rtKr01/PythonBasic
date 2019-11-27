name = input("Podaj imię: ")  # input zwraca string
lastname = input("Podaj nazwisko: ")
birthdate = input("Podaj datę urodzenia (YYYY-MM-DD): ")
position = input("Podaj stanowisko: ")
salaryNet = float(input("Wprowadź wynagrodzenie netto"))  # konwersja string na float
print(name, lastname, birthdate, position, str(salaryNet) + "zł", str(salaryNet * 1.23), sep=' | ')

name = "Robert"
salary = 10000.
isActivated = True
element = 1
print(type(name), type(salary), type(isActivated), type(element))
