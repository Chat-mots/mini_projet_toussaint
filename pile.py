class pile:
    """ classe définissant le tad PILE
        ---
        ATTRIBUTS :
                p : LISTE : Contenu de la pile
                nbr_elements: nombre d'éléments dans la pile (accessoire)
        ---
        METHODES :
            est_vide : -> BOOLEEN : return VRAI si la pile est vide, FAUX sinon
            empiler : ELEMENT -> VOID : ajoute un élément dans la pile
            depiler : -> ELEMENT : retire l'élément de la tête de la pile.
    """

    def __init__(self):
        self.p = []
        self.nbr_elements = 0

    def empiler(self, element):
        """
        méthode qui empile l'élément element dans la pile
        -----
        element : n'importe quoi qui peut être mis dans une pile
        -----
        pas de renvoie
        """
        self.p.append(element)
        self.nbr_elements += 1

    def est_vide(self):
        """
        vérifie si la pile est vide
        ---
        renvoie True si elle l'est, False sinon
        """
        return self.nbr_elements == 0

    def depiler(self):
        """
        méthode qui dépile l'élément element de la pile
        -----
        element : n'importe quoi, présent dans la pile
        -----
        aucun renvoie
        """
        element = None
        if not self.est_vide():
            element = self.p[-1]
            del(self.p[-1])
            self.nbr_elements -= 1
        return element

    def dernier(self):
        """
        méthode qui affiche l'élément element au sommet de la pile
        -----
        element : peut-être n'importe quoi, empilé au sommet de la pile
        -----
        renvoie l'élément en tête de pile
        """
        element = None
        if not self.est_vide():
            element = self.p[-1]
        return element

    def visualiser(self):
        """
        méthode affichant, élément par élément, le contenu de la pile
        -----
        liste : prend un a un les éléments de la pile
        -----
        renvoie les éléments de la pile un par un
        """
        liste = []
        for x in self.p:
            print("PILE : ", x)
            liste.append(x)
        print(liste)
        return liste


if __name__ == "__main__":

    p = pile()
    print(isinstance(p, int))
    assert(p.est_vide()) == True
    assert(p.dernier()) == None
    print(p.est_vide())
    p.empiler("UP")
    assert(p.est_vide()) == False
    p.empiler("DOWN")
    assert(p.dernier()) == "DOWN"
    print(p.depiler())
    p.empiler("TRIGHT")
    print(p.est_vide())
    print(p.depiler())
    print(p.est_vide())
    p.empiler("INIT")
    assert(p.est_vide()) == False
    p.visualiser()
