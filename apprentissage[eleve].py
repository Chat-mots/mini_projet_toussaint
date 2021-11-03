from sys import intern
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
        renvoie une liste chainé avant arrière en ayant converti les subroutines
        """
        lcaa = liste_chaine_AA()
        cel_lcaa = lcaa.racine
        
    def transfert_file(self,lc):
        pass
    
    def executer(self,f):
        pass
        
if __name__ == "__main__":
    prog = programme()