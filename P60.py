from math import sqrt


def calculateDistance(x,y): #liczenie na płaszczyźnie
    return round(sqrt(pow(y[0]-x[0],2)+pow(y[1]-x[1],2)),2)

p1=[1,1]
p2=[-2,-12]
print(calculateDistance(p2,p1))

def calculateDistance3D(p1,p2): #wersja trzy dy
    return round(sqrt(pow(p2[0]-p1[0],2)+pow(p2[1]-p1[1],2)+pow(p2[2]-p1[2],2)),2)

p1=[-5,-1,5]
p2=[-2,5,1]
print(calculateDistance3D(p2,p1))