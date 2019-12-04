# importy sa adresowane od katologu domowego -> nazwa projektu
# nazwa modułu występuje bez rozszerzenia
import Imports.SecrecVariables as sv
for i in dir(sv):
    print(i)
help(sv)


#dostęp do zmiennych

# print(sv.database) #alias zastępuje wszsytko co jest w adresie modułu razem z jego nazwą
# print(sv.password)
# print(sv.port)
# print(sv.host)
# print(sv.username)
#
# #dostęp do metod
# print(sv.getConnection())
#
# #dostęp do klas
# obiektKlasyZaimportowanej=sv.Hello("Michał")
# print(obiektKlasyZaimportowanej)