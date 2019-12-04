#program dziekanat
# -> klasa modelu Student: index,name,lastname,grades[]
#-> klasa logiki biznesowej addStudent(), getStudents(),deleteStudentByIndex()
#metoda uruchomieniowa poza powyższymi klasami (takie graphical user interface GUI lub Comand Line Interface CLI
#GUI użytkownika
from P67.controller.StudentController import StudentController

def commandLineInterface():
    sc=StudentController()
    while(True):
        try:
            print("Aplikacja Dziekanat")
            choice=input(" (I) - dodaj studenta\n (S) - wypisz studentów\n (G) - dodaj ocenę\n (D) - usuń studenta\n (Q) - wyjście")
            if(choice.upper()=="I"):
                data=input("Podaj numer indeksu,imię i nazwisko (po spacji)").split(" ")
                sc.addStudent(data[0],data[1],data[2])
            elif(choice.upper()=="S"):
                sc.getStudents()
            elif (choice.upper() == "G"):
                data=input("Podaj numer indeksu oraz ocenę, którą chcesz przypisać (po spacji)").split(" ")
                sc.addGradeToStudent(data[0],float(data[1]))
            elif (choice.upper() == "D"):
                data = input("Podaj numer indeksu studenta, którego chcesz usunąć")
                sc.deleteStudentsByIndex(data)
            elif (choice.upper() == "Q"):
                print("Wyjście")
                break
            else:
                print("Błędny wybór")
        except:
             print("ups! cos się wzieło i z... zepsuło")


commandLineInterface()