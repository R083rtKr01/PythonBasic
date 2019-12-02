#inicializacja wartości globalnej w skrypcie

globalId=0
class Player:
    def __init__(self, name, lastname, repr, weight, height):
        self.name = name
        self.lastname = lastname
        self.repr = repr
        self.weight = weight
        self.height = height
        global globalId    #modyfikacja wartości globalnej w skrypcie
        globalId+=1       #global -> wskaźnik globalny niezwiązany z klasą PLAYER
        self.id=globalId   #self_-> id dla konkretnego obiektu
    def calculateBMI(self):
        return self.weight/pow(self.height/100,2)
    def __str__(self):
        return ("| %3d | %10s | %10s | %10s | %10d | %10d | %10.2f |" %
                (self.id,
                 self.name,
                 self.lastname,
                 self.repr,
                 self.weight,
                 self.height,
                 self.calculateBMI()))


p1 = Player("Robert", "Król", "POL", 112, 185)
p2 = Player("Robert", "Lewandowski", "POL", 78, 185)
p3 = Player("Krzysztof", "Piątek", "POL", 77, 183)

print(p1,p2,p3)

players = [p1,p2,p3]
def getPlayers():
    for player in players:
        print(player)
def findPlayerById(findId):
    for player in players:
        if(player.id==findId):
            print(player)
getPlayers()
print()
findPlayerById(1)