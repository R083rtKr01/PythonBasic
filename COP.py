from datetime import date


class Auto:
    # klasa moze w sobie zawierać pola klasowe czyli obiekty, oraz zmienne
    brand ="b/d"
    model = "b/d"
    #metody klasowe -> czyli funkcje
    # zarówno pola klasowe jak i metody klasowe żyją tak długo jak klasy.
    #klasa jest pewnym szablonem zachowań
    def helloInClass(self):     # zapis "self" który obiekt wywołuje daną metodę
        return "witaj w programowaniu obiektowym"
#utworzenie obiektu
a= Auto()
print(a.helloInClass())
a.brand="BMW"
a.model="X3"
print(a.brand,a.model)

a1=Auto()
print(a1.brand,a1.model)

class User:
    def __init__(self,login,password,status,registrationDate): # metoda wywoływania jako pierwsz po utworzeniu obiektu
        #pole klasowe
        self.login=login
        self.password=password
        self.status=status
        self.registrationDate=registrationDate
    def setStatus(self,status): #modyfikacja status na wartośc podaną w argumencie

        self.status=status

    #funkcje specjalne czyli to rozpoczynające się od podwójnej podłogi __
    def __str__(self): # wywoływana gdy obiekt jest rzutowany do napisu
        return ("|%10s|%10s|%8s|%10s|"%(self.login,self.password,self.status,self.registrationDate))
    # del __del__(self):
    print("Obiekt został ")
u1= User("stefan","grahamka",True,date.today())
print(u1.login,u1.password,u1.status,u1.registrationDate)
print(u1)
u2=User("Robert","mrugacz13",False,date.today())
print(u2.login,u2.password,u2.status,u2.registrationDate)
u3 =u2
print("przed",u2.status,u3.status)
u2.status=True
print("po",u2.status,u3.status)
u1.setStatus(False)
print(u1)
print(u2)
print(u3)

print(u1.__class__.__name__) #określenie typu klasu.
print(type(u1))

u4=User("x","x",True)
u5=User("x","x",True,registrationDate="2000-02-02")
print(u4)
# print(u5.__del__())
# print(u5)

#napisz program OOP ktory reprezentuje skłądowe barw RGB
#implementacja klasy modelu reprezentujacej dowolny kolor




