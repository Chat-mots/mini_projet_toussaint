from cellule import *


class liste_chaine_AA:
    """
     ATTRIBUTS :
        classe definisant une liste chainée avant arrière
     racine : CELLULE : la cellule racine de la liste

     METHODES :
     est_vide : -> BOOLEEN : retourne VRAI si la liste est vide, FAUX sinon.

     ajouter : CELLULE -> CELLULE: ajoute une cellule à la fin de la liste et
        retourne l'@ de la cellule

     inserer : CELLULE,CONTENU -> CELLULE: ajoute une cellule après la
        cellule c et retourne l'@ de la cellule

     supprimer : supprime la cellule cellule_sup.

     trouver: CONTENU -> CELLULE: retourne l'@ de la première cellule dont le
        contenu est contenu.
    """

    def __init__(self) -> None:
        self.racine = cellule()

    def est_vide(self):
        """
        permet de savoir si la lcaa est vide ou pas.
        ---
        renvoie True si c'est vide, False sinon
        """
        if self.racine.suivant is None:
            return True
        else:
            return False

    def ajouter(self, c):
        '''
        ajoute une cellule de contenu c à la fin de la lcaa
        ---
        c : contenu à ajouter, peut être n'importe quoi
        ---
        renvoie la cellule qui vient d'être ajouté
        '''
        cell = cellule()
        cell.modifier(c)
        cel_courant = self.racine

        while cel_courant.suivant is not None:
            cel_courant = cel_courant.suivant

        cell.prec = cel_courant
        cel_courant.suivant = cell
        return cell

    def parcourir(self):
        cel_courant = self.racine
        liste_index = []

        while cel_courant.suivant is not None:
            liste_index.append(cel_courant)
            cel_courant.afficher()
            print("\n")
            cel_courant = cel_courant.suivant

            if cel_courant.suivant is None:
                liste_index.append(cel_courant)
                cel_courant.afficher()
                print("\n")
        return liste_index

    def inserer(self, p, c):
        """
        permet d'inserer une cellule de contenu p après la cellule d'index c
        ----------
        p: contenu de la cellule
        c: index de la cellule
        """
        cel_ajout = cellule()
        cel_ajout.modifier(p)
        baladeur = 0
        cel_courant = self.racine
        objectif = c
        cel_courant_suivant = self.racine

        while baladeur != objectif:
            cel_courant = cel_courant.suivant
            baladeur += 1
            if cel_courant.suivant is None:
                return "la valeur entrée est out of range"
        baladeur = 0

        while baladeur != objectif+1:
            cel_courant_suivant = cel_courant_suivant.suivant
            baladeur += 1

        cel_ajout.prec = cel_courant
        cel_ajout.suivant = cel_courant_suivant
        cel_courant_suivant.prec = cel_ajout
        cel_courant.suivant = cel_ajout

    def trouver(self, contenu):
        liste_index = chaine.parcourir()
        trouvee = None
        baladeur = 0

        while trouvee != contenu:
            if baladeur > len(liste_index)-1:
                print('contenu introuvable, il est inexistant')
                return "introuvable"
            if liste_index[baladeur].contenu == contenu:
                trouvee = contenu
            baladeur += 1

        return liste_index[baladeur-1]

    def supprimer(self, cellule_sup):
        baladeur = 0
        liste_index = chaine.parcourir()
        cel_courant = self.racine
        cel_prec = self.racine
        cel_suiv = self.racine

        for x in range(cellule_sup):
            cel_courant = cel_courant.suivant

        for h in range(cellule_sup-1):
            cel_prec = cel_prec.suivant

        for w in range(cellule_sup+1):
            cel_suiv = cel_suiv.suivant

        cel_prec.suivant = cel_suiv
        if cel_suiv is not None:
            cel_suiv.prec = cel_prec

        return print("la cellule d'index ", cellule_sup, " a été supprimé")


chaine = liste_chaine_AA()

if __name__ == "__main__":
    chaine.ajouter("a")
    chaine.ajouter("b")
    chaine.ajouter('c')
    print(chaine.inserer("poil", 2))
    print(chaine.trouver("a"))
    print(chaine.supprimer(2))
    print(chaine.parcourir())
    chaine.supprimer(0)
    print(chaine.parcourir())
    print(chaine.racine.suivant.contenu)