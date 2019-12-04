#klasa do obsługi żądań uzytkownika pochodzących z widoku typu html, CLI, Window
# implementacja logiki aplikacji
import datetime

from P67.model.Student import Student


class StudentController:
    students=[]
    # konstruktor pobranie i aktualizacja listy studentów z pliku
    def __init__(self):
        inputFile=open("database.csv","r") #otwarcie pliku do odczytu
        for index,line in enumerate(inputFile.readlines()):
            if(index==0):
                print(line) # wypisujemy datę aktualizacji
                continue
            # kazda linijkę z pliku mapujemy
            rowData=line.split(";")
            #czyszczenie napisu zawierajacego oceny z ([],)
            grades = rowData[3].replace("[","").replace("]","").split(", ")
            #konwersja ocena na float
            try:
                for index,grade in enumerate(grades):
                    grades[index]=float(grade)
            except:
                grades=[]
            #utworzenie obiektu studenta na podstawie danych z jednej lini pliku
            s=Student(rowData[0],rowData[1],rowData[2],grades)
            print(grades)
            #zapis zmapowanego obiektu do listy students
            self.students.append(s)
            # print(line,end="")
        inputFile.close()                   # zamknięcie strumienia danych do pliku
    # metoda dodająca studenta do listy
    def addStudent(self,index,name,lastname):
        if(self.validateStudentIndex(index)):
            #utworzenie obiektu studenta => odwołuje się do modelu
            s=Student(index,name,lastname)
            self.students.append(s)
            print("Dodano: ",s)
        else:
            print("Istnieje student o wskazanym indeksie")
    #metoda Walidacji danych studenta
    def validateStudentIndex(self,ValidateIndex):
        for student in self.students:
            if(student.index==ValidateIndex):
                #sprawdzamy czy juz istnieje taki indeks
                return False #nie dodajemy do listy
        return True     #dodajemy do listy
    #metoda dodająca ocenę
    def addGradeToStudent(self,inputindex,grade):
        # wyszukaj studenta po indexie
        gradeTemplate=[2,3,3.5,4,4.5,5,5.5]
        if (grade in gradeTemplate):
            isAdded = False
            for student in self.students:
                if(student.index==inputindex):
                    isAdded = True
                    student.addGrade(grade)
                    print("Dodano ocenę")
            #wypisz zaaktualizowaną listę studentów
            if (isAdded==False):
                print("Nie ma sudenta o takim indeksie")
                self.getStudents()
        else:
            print("podałeś niepoprawną ocenę")
    #metoda do usuwania studenta po indeksie
    def deleteStudentsByIndex(self,inputIndex):
        for student in self.students:
            if(student.index==inputIndex):
                print("Usunięto",student)
                self.students.remove(student)
        self.getStudents()
    #metoda wypisujaca wszystkich studentów z listy studentów
    def getStudents(self):
        print("|%6s|%15s|%15s|%20s|%7s"%
              ("INDEKS","IMIE","NAZWISKO","OCENY","ŚREDNIA"))
        for student in self.students:
            print(student)
    def __del__(self): # destruktor wywołuje się automatycznie gdy niszczony jest obiekt z pp
        outputFile = open("database.csv","w")
        outputFile.write("data aktualizacji:"+str(datetime.datetime.now())+ "\n")
        for student in self.students:
            outputFile.write(student.index+";"+student.name+";"+student.lastname+
                             ";"+str(student.grades)+";"+str(student.calculateAVG())+"\n")
            #zamknięcie strumienia danych
        outputFile.close()


#testowanie kontrolera
# sc=StudentController()
# sc.addStudent(123123,"test","test")
# sc.addStudent(123143,"test1","test1")
# sc.addStudent(123144,"test2","test2")
# sc.addStudent(123145,"test3","test3")
# sc.getStudents()

# sc.addGradeToStudent(123123,4)
# sc.addGradeToStudent(123123,2)
# sc.addGradeToStudent(1223123,4)
# sc.addGradeToStudent(123144,2)
# sc.addGradeToStudent(123144,5)
# sc.addGradeToStudent(123145,4)
# sc.addGradeToStudent(123143,5)
# sc.addGradeToStudent(123143,5)
# sc.addGradeToStudent(123143,5)
