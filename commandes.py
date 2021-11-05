from pile import *
from config import *
from programme import *

mapile = pile()


def commande():

    entre = 0

    while entre != "FIN":

        entre = input("commande : ")
        test = verifier(entre)

        if test is True:
            mapile.empiler(entre)

            if entre == "REM":
                mapile.depiler()
                if mapile.est_vide() is True:
                    print("la pile est déjà vide !")
                else:
                    mapile.depiler()
                    print("dépiler ! -> ", mapile.p)

            if entre == "VIEW":
                mapile.depiler()
                print("voici les actions : ", mapile.p)

        else:
            if entre != "FIN":
                print("votre commande est érroné, elle n'a pas été empiler")

    mapile.depiler()  # on enlève le FIN de la pile
    print("votre pile de commande ressemble à ceci : ", mapile.p)
    print("votre pile contient ", mapile.nbr_elements, " actions.")

    return mapile.p


def verifier(averifier):

    essai = len(commandes_base)

    for x in commandes_base:
        if averifier == x:
            return True
        else:
            essai -= 1

            if essai == 0:
                essai = len(commandes_sr)

                for x in commandes_sr:

                    if averifier == x.racine:
                        return True

                    else:
                        essai -= 1

                        if essai == 0:
                            essai = len(commandes_prog)

                            for x in commandes_prog:
                                if averifier == x:
                                    return True

                                else:
                                    essai -= 1

                                    if essai == 0:
                                        return False


if __name__ == "__main__":
    prog = Programme()
    prog.import_sr()
    print(commande())
