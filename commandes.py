from pile import *
from config import *

pile = pile()

def commande():

    entre = 0
    
    while entre != "FIN":
        
        entre = input("commande : ")
        test = verifier(entre)

        if test == True:
            pile.empiler(entre)

            if entre == "REM":
                pile.depiler()
                pile.depiler()
                print("dépiler ! -> ", pile.p)

            if entre == "VIEW":
                pile.depiler()
                print("voici les actions : ", pile.p)
        
        else:
            if entre != "FIN":
                print("votre commande est érroné, elle n'a donc pas été empiler")

    print("votre pile de commande ressemble à ceci : ", pile.p)
    print("votre pile contient ", pile.nbr_elements," actions.")
    
    return pile.p

def verifier(averifier):

    essai = len(commandes_base)
    
    for x in commandes_base:
        if averifier == x:
            return True
        else: 
            essai -= 1

            if essai == 0:
                return False

    essai = len(commandes_prog)

    for x in commandes_prog:
        if averifier == x:
            return True
        else:
            essai -= 1
        
            if essai == 0:
                return False
    
    essai = len(commandes_sr)

    for x in commandes_sr:
        if averifier == x:
            return True
        else:
            essai -= 1
        
            if essai == 0:
                return False


if __name__ == "__main__":
    commande()