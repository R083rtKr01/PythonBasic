def fibonacciSeries(n):

    if(n==0):
        return[]
    if(n==1):
        return[1]
    fibo = [0,1]
    cumSum = 1
    for i in range(2,n):
        fibo.append(fibo[i-1]+fibo[i-2])
        cumSum +=fibo[i]
    return (fibo,fibo[len(fibo)-1] ,cumSum)
print(fibonacciSeries(12))
print(fibonacciSeries(1))
print(fibonacciSeries(0))