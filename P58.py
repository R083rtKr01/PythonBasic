def fibo(n):  # definicja funkcji

    wrotka = (0, 1)  # dwa pierwsze wyrazy ciągu zapisane w tupli
    a, b = wrotka  # przypisanie wielokrotne, rozpakowanie tupli
    print(a, end=" ")
    while n > 1:
        print (b, end=" ")
        a, b = b, a + b  # przypisanie wielokrotne
        n -= 1

fibo(5)

def fiboR(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fiboR(n - 1) + fiboR(n - 2)
fiboR(5)

