from sys import intern
from file_circ import *
from pile import *
from config import *
from lcAA import *
from commandes import *
from cellule import *

class programme:
    """
    appli d'apprentissage pour le bras
    """
    
    def __init__(self):
        pass
        
    def gestion_commandes(self):
        pass
                    
    def import_sr(self,nom_fich=fich_sr):
        with open(nom_fich, 'r') as sr:
            lignes  = sr.readlines()
            for ligne in lignes:
                l = liste_chaine_AA()
                ligne = ligne[:-1]
                ligne = ligne.split(";")
                l.racine.contenu = ligne[0]
                for x in range(1,len(ligne)):
                    l.ajouter(ligne[x])
                commandes_base.append(l.racine.contenu)
                commandes_sr.append(l)

    def trouver_sr(self,nom):
        pass
                
    def homogenise(self):
        """
        transforme la pile que lui a envoyé gestion_commandes
        ---
        renvoie une liste chainée avant arrière en ayant converti les subroutines
        """
        lcaa = liste_chaine_AA()
        cel_lcaa = lcaa.racine
        index = 0
        self.pile = ['UP','INIT','DOWN']
        mafile = File_circ(len(self.pile)+10)
        for x in self.pile:
            lcaa.ajouter(x)
            for test in range(len(commandes_sr)): # test devient l'index d'une liste chainé dans commandes_sr
                liste = commandes_sr[test] # liste est une liste chainé de commandes_sr
                if x == liste.racine.contenu: # si l'action entrée est égal au contenu de la racine, c'est à dire le nom, exemple : INIT
                    cel_courant = liste.racine
                    # print('1 : ',cel_courant.contenu)
                    cel_courant = cel_courant.suivant
                    # print('2 : ', cel_courant.contenu)
                    
                    while cel_courant.suivant != None:
                        lcaa.ajouter(cel_courant.contenu)
                        # print("3 : ", cel_courant.contenu)
                        cel_courant = cel_courant.suivant
                    lcaa.ajouter(cel_courant.contenu)
            while cel_lcaa.suivant != None: # problème : ne marche qu'une fois, pourquoi ?
                for test in range(len(commandes_sr)):
                    cel_test = commandes_sr[test].racine.contenu
                    if cel_test == cel_lcaa.contenu:
                        lcaa.supprimer(index)
                        index-=1
                cel_lcaa = cel_lcaa.suivant
                index += 1
            lcaa.parcourir()

        cel_lcaa = lcaa.racine.suivant

        while cel_lcaa.suivant != None:
            mafile.enfiler(cel_lcaa.contenu)
            cel_lcaa = cel_lcaa.suivant
        mafile.enfiler(cel_lcaa.contenu)
        
        print(mafile.file)
        return mafile

    def transfert_file(self,lc):
        pass
    
    def executer(self,f):
        pass
        
if __name__ == "__main__":
    prog = programme()
    prog.import_sr()
    prog.homogenise()
    # regarder la liste pour vérifier que tout marche bien :
    print(prog.homogenise())