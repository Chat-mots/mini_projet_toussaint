from sys import intern
from file import File
from file_circ import *
from pile import *
from config import *
from lcAA import *
from commandes import *
from cellule import *
import copy


class Programme:
    """
    appli d'apprentissage pour le bras
    """

    def __init__(self):
        pass

    def gestion_commandes(self):
        commande()

    def import_sr(self, nom_fich=fich_sr):
        """
        transforme les instructions de subroutines dans sr.txt en lcaa
        ---
        crée une lcaa par subroutine
        """
        with open(nom_fich, 'r') as sr:
            lignes = sr.readlines()
            for ligne in lignes:
                liste = liste_chaine_AA()
                ligne = ligne[:-1]
                ligne = ligne.split(";")
                liste.racine.contenu = ligne[0]
                for x in range(1, len(ligne)):
                    liste.ajouter(ligne[x])
                commandes_base.append(liste.racine.contenu)
                commandes_sr.append(liste)

    def trouver_sr(self, nom):
        pass

    def homogenise(self, pilerecu):
        """
        transforme la pile envoyé par gestion_commandes en lcaa et en file
        ---
        pilerecu : pile qui sera transformé en file
        ---
        renvoie une file de toutes les actions que devra effectuer le robot
        """
        lcaa = liste_chaine_AA()
        cel_lcaa = lcaa.racine
        index = 0
        # self.pile sera un DEEPCOPY de la pile reçu !!
        # sera le paramètre reçu par gestion_commande (bourrage en attendant)
        # self.pile = ['UP', 'INIT', 'DOWN']
        save = pilerecu
        self.pile = copy.deepcopy(save)

        # au cas où le paramètre reçu est une pile vide, on renvoie None
        if self.pile == []:
            print("la pile reçu est vide !")
            return None

        # transforme la pile reçu en lcaa
        for x in self.pile:
            # ajout d'une action dans la lcaa
            lcaa.ajouter(x)
            for test in range(len(commandes_sr)):
                liste = commandes_sr[test]
                # ajout d'une subroutine dans la lcaa
                if x == liste.racine.contenu:
                    cel_courant = liste.racine
                    cel_courant = cel_courant.suivant

                    while cel_courant.suivant is not None:
                        lcaa.ajouter(cel_courant.contenu)
                        cel_courant = cel_courant.suivant
                    lcaa.ajouter(cel_courant.contenu)
            while cel_lcaa.suivant is not None:
                for test in range(len(commandes_sr)):
                    cel_test = commandes_sr[test].racine.contenu
                    if cel_test == cel_lcaa.contenu:
                        lcaa.supprimer(index)
                        index -= 1
                cel_lcaa = cel_lcaa.suivant
                index += 1
            lcaa.parcourir()

        # ajout dans la file de toutes les actions du robots
        mafile = File()
        cel_lcaa = lcaa.racine.suivant
        while cel_lcaa.suivant is not None:
            mafile.enfiler(cel_lcaa.contenu)
            cel_lcaa = cel_lcaa.suivant
        mafile.enfiler(cel_lcaa.contenu)

        # pas obligatoire, vérification que la file est correcte
        print("la file ressemble à ceci : ", mafile.file)

        return mafile

    def transfert_file(self, lc):
        pass

    def executer(self):
        ex = commande()
        self.homogenise(ex)


if __name__ == "__main__":
    prog = Programme()
    prog.import_sr()
    prog.executer()
    # regarder la liste pour vérifier que tout marche bien :
    # test = commande()
    # prog.homogenise(test)
    # prog.gestion_commandes()
