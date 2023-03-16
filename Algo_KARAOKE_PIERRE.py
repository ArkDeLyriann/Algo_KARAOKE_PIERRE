#-----EXERCICE A-----#
import random
nouveauScore = 0  

class Player:
    def __init__(self, nom, points) -> None:
        self.__nom = nom
        self.__score = points
    
    def getName(self):
        return self.__nom
    def getScore(self):
        return self.__score

    def changeScore(self, nouveauScore):
        if self.__score < nouveauScore:
            self.__score = nouveauScore

 

j1 = Player ("1", 0)
j2 = Player ("2", 0)
j3 = Player ("3", 0)
j4 = Player ("4", 0)
partie = [j1,j2,j3,j4]


for j in range (0,4):
    print ("Chanson n°", j)
    for i in range (0, 4):
        nouveauScore = random.randint(50, 100)
        partie[i].changeScore(nouveauScore)
        nouveauScore = 0
        print (partie[i].getName(), "à", partie[i].getScore())

