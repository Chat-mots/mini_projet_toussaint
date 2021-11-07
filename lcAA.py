from cellule import *


class liste_chainee_AA:
    '''
    Liste sous la forme d'une chaîne composée de maillons (cellules),
    permettant l'insertion à n'importe quelle position d'un nouvel élément
    Attributs :
    -------------
    racine => instance de cellule : Première cellule de la racine, vide de
    contenu, servant à parcourir la liste
    Méthodes :
    -------------
    est_vide : Renvoie True si la liste ne contient que la racine, ou False le
    cas contraire
    ajouter : Ajoutes une nouvelle cellule au bout de la liste
    parcourir : Affiches chaque élément de la liste, sauf la racine
    inserer : Inseres une nouvelle cellule après un certain maillon
    trouver : Recherches un maillon selon son contenu et renvoit l'adresse
    mémoire du premier maillon possédant le contenu en question
    supprimer : Cherches un maillon avec une adresse particulière et le
    supprime '''

    def __init__(self) -> None:
        self.racine = cellule()
        self.racine.modifier("Je suis la racine")

    def est_vide(self):
        '''
        Fonction qui permet de savoir si la liste est vide
        Renvoit :
        -------------
        True si la liste est vide
        False inversement '''
        if self.racine.suivant is None:
            return True
        else:
            return False

    def ajouter(self, c):
        '''
        Fonction qui ajoutes une cellule à la fin de la liste
        Paramètres :
        -------------
        c => N'importe quel type de données : Le contenu de la cellule qu'on
        veut ajouter
        Renvoit :
        -------------
        cell : l'adresse de la cellule crée et ajoutée'''
        cell = cellule()  # Création de la cellule qui va être ajoutée
        cell.modifier(c)
        cel_courant = self.racine  # Permet de parcourir la liste

        while cel_courant.suivant is not None:  # On parcourt jusqu'à la fin
            # de la liste
            cel_courant = cel_courant.suivant

        cell.prec = cel_courant  # On ajoute la cellule cell
        cel_courant.suivant = cell
        return cell

    def parcourir(self):
        '''
        Fonction qui parcourt la liste en affichant le contenu de chaque
        cellule'''
        cel_courant = self.racine.suivant

        if cel_courant.suivant is None:  # S'il y a qu'un seul élément dans la
            # liste après la racine
            cel_courant.afficher()
        else:
            while cel_courant.suivant is not None:  # On affiche chaque élément
                # de la liste
                cel_courant.afficher()
                print("\n")
                cel_courant = cel_courant.suivant

                if cel_courant.suivant is None:  # On affiche le dernier
                    # élément, pas pris en compte par la boucle précédente.
                    cel_courant.afficher()
                    print("\n")

    def inserer(self, contenu, cellule):
        '''
        Fonction qui crée une nouvelle cellule et l'insère après une certaine
        cellule
        Paramètres :
        -------------
        contenu => N'importe quel type de données: Le contenu de la future
        cellule qu'on veut insérer
        cellule => instance de cellule (adresse mémoire) : La cellule où on
        veut insérer notre cellule
        Renvoit :
        -------------
        ajout : l'adresse de la cellule nouvellement crée et
        insérée'''
        ajout = cellule()  # On crée la cellule qui va être insérée
        ajout.modifier(cellule)
        cel_courant = self.racine
        err = False

        if cellule.suivant is None:  # Si on souhaite insérer une cellule au
            # bout de la file, on fait alors un ajout à la place
            ajout = self.ajouter(contenu)
        else:

            while cel_courant != cellule:
                if cel_courant.suivant is None:  # Si "cellule" n'existe pas
                    print("La cellule donnée n'existe pas dans la liste")
                    err = True
                cel_courant = cel_courant.suivant
            if err is False:  # Si on a bien trouvée "cellule"
                ajout.suivant = cel_courant.suivant
                ajout.prec = cel_courant
                cel_courant.suivant.prec = ajout
                cel_courant.suivant = ajout

                return cel_courant

    def trouver(self, contenu):
        '''
        Fonction qui recherche une cellule dans la liste avec un certain
        contenu
        Paramètres :
        -------------
        contenu => N'importe quel type de donnée : Le contenu à rechercher
        dans la liste
        Renvoit :
        -------------
        cel_courant : L'adresse de la première cellule contenant le contenu
        recherché '''
        cel_courant = self.racine
        err = False
        while cel_courant.contenu != contenu:
            if cel_courant.suivant is None:  # Si aucune cellule ne possède
                # comme contenu le paramètre
                print("Aucune cellule trouvée")
                err = True
            cel_courant = cel_courant.suivant
        if err is False:
            return cel_courant

    def supprimer(self, cellule_sup):
        '''
        Fonction qui supprime une cellule de la liste
        Paramètres :
        -------------
        cellule_sup => instance de cellule : La cellule que l'on veut
        supprimer'''
        cel_courant = self.racine
        err = False
        while cel_courant != cellule_sup:  # Si "cellule_sup" n'existe pas dans
            # la liste
            if cel_courant.suivant is None:
                err = True
                print("Cellule à supprimer non existante dans la liste")
            cel_courant = cel_courant.suivant
        if err is False:
            cel_courant.prec.suivant = cel_courant.suivant
            if cel_courant.suivant is not None:
                cel_courant.suivant.prec = cel_courant.prec


chaine = liste_chainee_AA()

if __name__ == "__main__":
    chaine.ajouter("a")
<<<<<<< HEAD
    futur_sup = chaine.ajouter("b")
    # chaine.parcourir()
    chaine.supprimer(futur_sup)
    chaine.parcourir()
=======
    chaine.ajouter("b")
    chaine.ajouter('c')
    # print(chaine.inserer("poil", 2))
    print(chaine.trouver("a"))
    print(chaine.supprimer(2))
    # print(chaine.parcourir())
    # chaine.supprimer(0)
    print(chaine.parcourir())
    # print(chaine.racine.suivant.contenu)
>>>>>>> f6a9c61519c1ec324bf3fe0a4e1aeb3e3b62b268
