try:
    number = input("Podaj Liczbę")
    number = float(number) # miejsce w którym możę wystąpićbłąd
except:
    result=float(len(number))

print(type(result),result)
