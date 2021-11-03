class File_circ :

    def __init__(self,n) :
        """
        ATTRIBUTS :
            classe définissant une file circulaire
        file : liste représentant la file
        tmax : le nombre d'élément de la file
        index_début : indique quel est le premier élément de la file
        index_fin : indique quel est le dernier élement de la file
        """
        self.file = [None for x in range(n)]
        self.tmax = n
        self.index_debut = 0
        self.index_fin = 0
        self.nbr_elements = 0

    def est_vide(self) :
        if self.nbr_elements == 0 :
            return True
        else :
            return False

    def enfiler(self,element) :
        if self.nbr_elements < 6 :
            self.file[self.index_fin] = element
            self.nbr_elements += 1
            if self.index_fin < self.tmax - 1 :
                self.index_fin += 1
            elif self.index_fin == self.tmax -1 :
                self.index_fin = 0

    def defiler(self) :
        if self.est_vide() == False :
            element = self.file[self.index_debut]
            if self.index_debut == 5 :
                self.index_debut = 0
            else :
                self.index_debut += 1
            self.nbr_elements -= 1
            return element

    def nombre_elements(self) :
        nbr = self.index_fin-self.index_debut
        if nbr == -1 : 
            nbr = 6
        return nbr


            

if __name__ == "__main__" :
    file = File_circ(6)
    assert(file.est_vide()) == True
    assert(file.tmax) == 6
    assert(file.est_vide()) == True
    for x in range(6) :
        file.enfiler("test")
    assert(file.index_fin) == 0
    assert(file.nbr_elements) == 6
    assert(file.est_vide()) == False
    for x in range(6) :
        file.defiler()
    assert(file.index_debut) == 0
    assert(file.nbr_elements) == 0
    print("done")

