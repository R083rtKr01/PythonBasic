from random import randint


def generateNrandomElements(n):
    elements=[]
    for i in range(n):
            elements.append(randint(-1000,1000))
    print(elements)
    return elements
print(generateNrandomElements(10))

def getElementsSupportMTreshold(n,treshold): #minSupp to wattość progowa
    elementsSupportTreshold = []
    cumSum=0
    for elem in generateNrandomElements(n):
        if(elem>treshold):
            cumSum +=elem
            elementsSupportTreshold.append(elem)
    return elementsSupportTreshold, cumSum

print(generateNrandomElements(10))
print(getElementsSupportMTreshold(10,0))