# import z określonej lokalizacji konkretnych składowych
#   składowe sa dostępne bez adresownia
from Imports.SecrecVariables import Hello
from Imports.SecrecVariables import getConnection
from Imports.SecrecVariables import database,username,password
import Imports.SecrecVariables as secret



#ctrl +alt + O -> optymalizuje do wykorzystanych zmiennych klas i metod. O jak Ola

print(username)
print(password)
print(database)
# print(port) nie będzie pokazany bo nie został zaimportowany zaciągniety z SecrecVariables
h=Hello("RK")
print(h)
print(getConnection())
