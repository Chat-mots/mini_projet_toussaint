class File_circ:
    """
    classe définissant une file circulaire
    ---
    ATTRIBUTS :
    file : liste représentant la file
    tmax : le nombre d'élément de la file
    index_début : indique quel est le premier élément de la file
    index_fin : indique quel est le dernier élement de la file
    ---
    METHODES :
    est_vide : renvoie True si la file est vide, False sinon
    enfiler: enfile un élément dans la file
    defiler : defile l'élément à sortir selon la règle du
        premier entré, premier sorti
    nombre_elements : renvoie le nombre d'élément présent dans la file
    """

    def __init__(self, n):
        self.file = [None for x in range(n)]
        self.tmax = n
        self.index_debut = 0
        self.index_fin = 0
        self.nbr_elements = 0

    def est_vide(self):
        """
        renvoie True si la file est vide, False sinon
        """
        if self.nbr_elements == 0:
            return True
        else:
            return False

    def enfiler(self, element):
        """
        enfile l'objet "element" dans la file selon la règle du
            premier entré, premier sorti
        """
        if self.nbr_elements < 6:
            self.file[self.index_fin] = element
            self.nbr_elements += 1
            if self.index_fin < self.tmax - 1:
                self.index_fin += 1
            elif self.index_fin == self.tmax - 1:
                self.index_fin = 0

    def defiler(self):
        """
        defile l'objet prêt à sortir de la file selon
            la règle du premier entré, premier sorti
        """
        if self.est_vide() is False:
            element = self.file[self.index_debut]
            if self.index_debut == 5:
                self.index_debut = 0
            else:
                self.index_debut += 1
            self.nbr_elements -= 1
            return element

    def nombre_elements(self):
        """
        renvoie le nombre d'élément présent dans la file
        """
        nbr = self.index_fin-self.index_debut
        if nbr == - 1:
            nbr = 6
        return nbr


if __name__ == "__main__":
    file = File_circ(6)
    assert(file.est_vide()) is True
    assert(file.tmax) == 6
    assert(file.est_vide()) is True
    for x in range(6):
        file.enfiler("test")
    assert(file.index_fin) == 0
    assert(file.nbr_elements) == 6
    assert(file.est_vide()) is False
    for x in range(6):
        file.defiler()
    assert(file.index_debut) == 0
    assert(file.nbr_elements) == 0
    print("done")
