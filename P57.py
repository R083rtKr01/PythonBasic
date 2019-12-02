# zrobić n silnia n!
#n!=n*(n-1)*(n-2)*(n-3)

def factorial(n):
    result = 1
    while(n>1):
        result *= n # result = result *n
        n-= 1
    return result

n = 6
print("%d!=%d"% (n,factorial(n)))

def factorialRec(n):
    if(n==2):
        return n
    return n* factorial(n-1)

n=8
print(factorialRec(n))