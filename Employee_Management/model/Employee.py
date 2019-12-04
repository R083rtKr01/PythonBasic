from Employee_Management.model.Trainee import Trainee
from enum import Enum


# typ wyliczeniowy - dopuszcza tylko wybrane możliwości
class Permission(Enum):
    ROLE_EMPL = 1
    ROLE_MAN = 2
    ROLE_HEAD = 3


class Employee(Trainee):
    def __init__(self, name, lastname, login, password,
                 possition,salary, permission=Permission.ROLE_EMPL):
        super().__init__(name, lastname, login, password)
        self.possition = possition
        self.salary = salary
        self.permission = permission

    def __str__(self):
        return super().__str__() + " %5s |" % (self.permission.value)


# e = Employee("Robert", "Król", "Rkrol", "Jureczki13", "Junior Data Analyst",
#              5000, Permission.Role_empl)
# e1 = Employee("Stefan", "Bliski", "Sbliski", "Stefek13", "Senior Data Analyst",
#               15000, Permission.Role_man)
# e.assignPrise(2000)
# print(e)
# print(e1)
