database="python_db"
username="root"
password="123"
port=3306
host="localhost"

def getConnection():
    return"Connected"

class Hello:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "hello %s"%(self.name)