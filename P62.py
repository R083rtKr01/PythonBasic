#średnia arytmetyczna dla dowolnej liczby argumentów, lub 0 jeśli liczba argumentów =0

def nonDefinedParameter(*elements):
    sum=0
    for elem in elements:
        sum+=elem
    return sum/len(elements)