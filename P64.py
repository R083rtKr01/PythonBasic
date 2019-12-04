#Napisz funkcję, która będzie wyświetlała przy
# każdym kolejnym wywołaniu na przemian nazwy
# dwóch kolorów: biały i czarny.

# funkcja odwołująca się do obiektu globalnego zadeklarowanego w skrypcie

def returnColour():
    global value #pobieram wartość globalną
    value=not value # modifukuje wartość globalną
    return "black" if value else "white"

value=True
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())
print(returnColour())
