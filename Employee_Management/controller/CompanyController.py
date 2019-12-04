import hashlib

from Employee_Management.model.Employee import Employee, Permission
from Employee_Management.model.Trainee import Trainee


class CompanyController:
    employees = [
        Employee("mk1", "mk1", "mk1", "mk1", "PYTHON DEV", 11000, Permission.ROLE_EMPL),
        Employee("mk2", "mk2", "mk2", "mk2", "JAVA DEV", 9000, Permission.ROLE_EMPL),
        Employee("mk3", "mk3", "mk3", "mk3", "PYTHON DEV", 12000, Permission.ROLE_EMPL),
        Employee("mk4", "mk4", "mk4", "mk4", "MANAGER", 14000, Permission.ROLE_MAN),
        Employee("mk5", "mk5", "mk5", "mk5", "SCRUM MASTER", 13000, Permission.ROLE_MAN),
        Employee("mk6", "mk6", "mk6", "mk6", "HEAD", 17000, Permission.ROLE_HEAD),
        Employee("mk7", "mk7", "mk7", "mk7", "HEAD", 21000, Permission.ROLE_HEAD),
        Employee("mk8", "mk8", "mk8", "mk8", "DEV OPS", 11500, Permission.ROLE_EMPL),
        Trainee("t1", "t1", "t1", "t1"),
        Trainee("t2", "t2", "t2", "t2"),
        Trainee("t3", "t3", "t3", "t3")
    ]

    # 1. dodawanie pracownika lub praktykanta z unikatowym loginem
    def addEmployeeOrTrainee(self, o):
        if (o.__class__.__name__ == "Trainee" or o.__class__.__name__ == "Employee"):
            if (self.loginValid(o.login)):
                print("Dodano Pracownika", o.name, o.lastname, o.possition)
                self.employees.append(o)
            else:
                print("Istnieje już taki login w naszej bazie danych")
        else:
            print("Dany obiekt: " + o + " nie jest pracownikiem ani praktykantem")

    # 1.* sprawdzenie czy dany login jnie istnieje w liscie employees
    def loginValid(self, login):
        for e in self.employees:
            if (e.login == login):
                return False
        return True

    # 2. wyświetlenie wszsytkich pracowników i praktykantów
    def getEmployees(self):
        # sortowanie po pensji
        for e in sorted(self.employees, key=lambda e: e.salary, reverse=True):
            print(e)

    # def getEmployees(self):
    #     # sortowanie po pensji
    #     for e in sorted(self.employees, key=lambda e:e.salary,reverse=True):
    #         print(e)

    # wyświetlenie tylko kierowników i dyrektorów po loginia A-Z
    def getManagersOrderByLogin(self):
        for m in self.employees:
            if (m.__class__.__name__ == "Employee"):
                if (m.permission.value in [2, 3]):
                    print(m)

    def getManagersOrderByLoginASC(self):
        result = filter(lambda m1: m1.__class__.__name__ == "Employee" and m1.permission.value in [2, 3],
                        self.employees)
        for m1 in sorted(result, key=lambda m1: m1.login, reverse=False):
            print(m1)

        # result= filter(lambda m : Permission=="Trainee",self.employees)
        # for m in sorted(result, key=lambda m:m.login ,reverse=True):
        #     print(m)
        # dlatego not ponieważ jedyną pozostałą grupą w firmie jest praktykant

    # wyświetlenie praktykantów po loginie

    def getTraineeOrderByLogin(self):
        result = filter(lambda t: t.__class__.__name__ == "Trainee", self.employees)
        for t in sorted(result, key=lambda t: t.login, reverse=True):
            print(t)

    # przypisanie nagrody/premi dla pracownika lub praktykanta
    def setPrise(self, amount, login=""):
        if (login != ""):
            islogin = False
            # wyszukja pracownika
            for e in self.employees:
                if (e.login == login):
                    e.assignPrise(amount)
                    islogin = True
                    break
            if (islogin == False):
                print("Błędny login pracownika")
        else:
            for e in self.employees:
                e.assignPrise(amount)
        self.getEmployees()

    # zmiana pensji tylko dla pracownika
    def changeEmployeeSalary(self, login, salary):
        isEmployee = False
        for e in self.employees:
            if (e.login == login and e.__class__.__name__ == "Employee"):
                e.salary = salary
                isEmployee = True
                break
        if (isEmployee == False):
            print("błędny login lub typ pracownika")
        self.getEmployees()

    # usuwanie pracownika lub praktykanta z listy pracowników
    def deleteEmployeeOrTrainee(self, login):
        for e in self.employees:
            if (e.login == login):
                self.employees.remove(e)
                print("Usunięto:", e.login)

    # za potwierdzeniem usunięcia ale hasłem bez tego nie usunie
    def deleteEmployeeOrTraineeWithPassConfirm(self, login):
        isFound = False
        for e in self.employees:
            isFound = True
            if (e.login == login):
                inputPasswd = (input("potwierdź usuwanie hasłem").strip(" "))
                if e.password == hashlib.md5(("salt:xyz" + inputPasswd).encode('utf-8')).hexdigest():
                    self.employees.remove(e)
                    print("Usunięto:", e.login)
                else:
                    print("błąd autoryzacji")
        if (isFound == False):
            print("Nie ma takiego pracownika")
