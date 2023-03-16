#-----EXERCICE A-----#
import random
#nouveauScore = 0
#storage = 0

#class Player:
    #def __init__(self, nom, points) -> None:
        #self.__nom = nom
        #self.__score = points
    
    #def getName(self):
        #return self.__nom
    
    #def getScore(self):
        #return self.__score

    #def changeScore(self, nouveauScore):
     #   if self.__score < nouveauScore:
      #      self.__score = nouveauScore

 

#j1 = Player ("1", 0)
#j2 = Player ("2", 0)
#j3 = Player ("3", 0)
#j4 = Player ("4", 0)
#partie = [j1,j2,j3,j4]


#for j in range (0, 4):
    #print ("-------------")                                                 
    #print ("Joueur n°", j+1)
    #print ("-------------")
    #for i in range (0, 5):
        #nouveauScore = random.randint(50, 100)
        #storage += nouveauScore
        #partie[j].changeScore(nouveauScore)
        #nouveauScore = 0
        #print ("Chanson n°",i+1, " score: ", partie[j].getScore())

    #print ("-------------")
    #moyenne = storage/5
    #storage = 0
    #print( "Moyenne du joueur : ", moyenne)#


#-----EXERCICE B-----#

nouveauScore = 0
storage = 0
choix = -1
moyenne = 0

class Player:
    def __init__(self, nom, scorebase) -> None:
        self.__nom = nom
        self.__scorebase = scorebase
        self.__scores = []

    def getName(self):
        return self.__nom
    
    def getScore(self):
        return self.__scores

    def changeScore(self, nouveauScore, position):
        self.__scores.insert(position, nouveauScore)
    
    
    def moyenne(self):
        for q in range (0, len(self.__scores)):
            storage += self.__scores[i]
        
        moyenne = storage/len(self.scores)
        print ("La moyenne de", self.getName(), "est de", moyenne)

    def bestScore(self):
        #algorythme de tri qui sauvegarde la plus grande valeur dans la liste des scores et la print

    def lowestScore(self):
        #algorythme de tri qui sauvegarde la plus petit valeur dans la liste des scores et la print    
 

j1 = Player ("J1", 0)
j2 = Player ("J2", 0)
j3 = Player ("J3", 0)
j4 = Player ("J4", 0)
partie = [j1,j2,j3,j4]


class Karaoke:
    def __init__(self, nbPlayer, chansons) -> None:
        self.__nbPlayer = nbPlayer
        self.__nbChansons = chansons
        player = partie
    
    def deletePlayer(self):
        if len(partie) <=1 :
            print("IMPOSSIBLE D'AVOIR MOINS D'UN JOUEUR")
        else:
            print (" quel joueur supprimer ? ")
            for i in range (0, len(partie)):
                print (partie[i].getName()," tapez", i)
            choix = input()
            partie.pop(choix)

    def addPlayer(self):
        nvJoueur = Player(input("Nom Joueur :"), 0)
        partie.append(nvJoueur)

        



for i in range (0, 3):
    nouveauScore = random.randint(50, 100)
    j1.changeScore(nouveauScore,i)
    print (j1.getScore())


#Je n'ai pas eu le temps de créer une boucle de jeu pour tester mes classes.

