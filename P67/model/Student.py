#klasa modelu determinuje strukture danych
#wspiera podejscie ORM object relationship mapping
# rzutuje cechy danych pochodzących z bazy danych np z tabelki SQL na obiekt python
class Student:
    def __init__(self,index,name,lastname,grades=[]):
        #to cechuje pojedynczego studenta
        self.index=index
        self.name=name
        self.lastname=lastname
        self.grades=grades
        #metoda do dodawania ocen do listy 'grades'
    def addGrade(self,grade):
        self.grades.append(grade)
    # metoda do zwracająca średnią ocen
    def calculateAVG(self):
        cumSum=0
        if(len(self.grades)==0):
            return 0
        for grade in self.grades:
            cumSum+=grade
        return cumSum/len(self.grades)
    def __str__(self):
        return"|%6s|%15s|%15s|%20s|%5s|"% (self.index,self.name,self.lastname,self.grades,
               "B/D" if self.calculateAVG()==0 else round(self.calculateAVG(),2))

#testowanie modelu

# s= Student(244632,"Robert","Król")
# s.addGrade(5)
# s.addGrade(2)
# s.addGrade(3)
# print(s)
