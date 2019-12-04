import hashlib


class Trainee:
    def __init__(self,name,lastname,login,password):
        self.name=name
        self.lastname=lastname
        self.login=login
        self.password=hashlib.md5(("salt:xyz"+password).encode('utf-8')).hexdigest()
        self.possition="Praktykant"
        self.salary=0
    def assignPrise(self,amount):
        self.salary+=amount
    def __str__(self):
        return"| %15s | %15s | %15s | %10s | %15s | %13.2fzł |"%\
               (self.name,self.lastname,self.login,self.password[0:8],self.possition,
                self.salary)

#test
# t=Trainee("Michał","Kruczkowski","MKruczko","Kruku13")
# t.assignPrise(-1000)
# print(t)
