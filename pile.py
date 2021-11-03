

class pile:
    """ classe définissant le tad PILE
        ATTRIBUTS :
                p : LISTE : Contenu de la pile
                nbr_elements : ENTIER : nombre d'éléments dans la pile (accessoire)
                
        METHODES :
            est_vide : -> BOOLEEN : retourne VRAI si la pile est vide, FAUX sinon.
            empiler : ELEMENT -> VOID : ajoute un élément dans la pile
            depiler : -> ELEMENT : retire l'élément de la tête de la pile.
    """
    
    def __init__(self):
        self.p=[]
        self.nbr_elements=0
        
    def empiler(self,element):
        self.p.append(element)
        self.nbr_elements+=1
        
    def est_vide(self):
        return self.p==[]
        
    
    def depiler(self):
        element=None
        if not self.est_vide():
            element = self.p[-1]
            del(self.p[-1])
            self.nbr_elements-=1
        return element
    
    def dernier(self):
        element=None
        if not self.est_vide():
            element = self.p[-1]
        return element
    
    def visualiser(self):
        liste = []
        for x in self.p:
            print("PILE : ",x)
            liste.append(x)
        print(liste)
        return liste

if __name__=="__main__":  
  
    p=pile()
    print(isinstance(p,int))
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
