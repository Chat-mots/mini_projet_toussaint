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
        méthode qui empile l'élément element dans la file
        -----
        element : n'importe quoi qui peut être mis dans une file
        -----
        pas de renvoie
        """
        self.p.append(element)
        self.nbr_elements += 1

    def est_vide(self):
        """
        vérifie si la file est vide
        ---
        renvoie True si elle l'est, False sinon
        """
        return self.nbr_elements == 0

    def depiler(self):
        element = None
        if not self.est_vide():
            element = self.p[-1]
            del(self.p[-1])
            self.nbr_elements -= 1
        return element

    def dernier(self):
        element = None
        if not self.est_vide():
            element = self.p[-1]
        return element

    def visualiser(self):
        liste = []
        for x in self.p:
            print("PILE : ", x)
            liste.append(x)
        print(liste)
        return liste


if __name__ is "__main__":

    p = pile()
    print(isinstance(p, int))
    print(p.est_vide())
    p.empiler("UP")
    p.empiler("DOWN")
    print(p.depiler())
    p.empiler("TRIGHT")
    print(p.est_vide())
    print(p.depiler())
    print(p.est_vide())
    p.empiler("INIT")
    p.visualiser()
