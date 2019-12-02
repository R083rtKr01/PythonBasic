# suma ciągu geometrycznego i n-ty element

def GeoAvg(n,a1=1,q=2):
    cumSum=0
    elements=[]
    for i in range(0,n):
        cumSum+= a1 * (q ** (n-1))
        elements.append(a1*pow(q,i))
    return cumSum, elements

print(GeoAvg(4,a1=3,q=2))