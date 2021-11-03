class File:
    '''
    une classe utilisé pour représenter des files.
    Comme une file d'attente par exemple.
    ----------
    Attributs : 
    ----------
    liste_file : list
        la liste qui servira à representer la file
    index_debut : int
        sa valeur indique où est ce que démarre la file
    index_fin : int
        sa valeur indique où est la fin de la file
    ----------
    Methodes :
    ----------
    est_vide()
        indique si la file est vide par un booléen
    enfiler(element)
        ajoute l'élément element à la fin de la file
    defiler()
        retire le premier élément à être rentré dans la file
    sommet()
        indique ce qu'est l'élément prêt à sortir (le sommet)
    nombre_elements()
        renvoie le nombre d'éléments son présent dans la file (excluant les vides)
    '''
    def __init__(self) -> None:
        self.liste_file = [None, None, None, None, None, None]
        self.index_debut = 0
        self.index_fin = 0

    def est_vide(self):
        '''
        permet de savoir si la file est vide
        ----------
        renvoie True si elle est vide,
        renvoie False si elle ne l'est pas
        ----------
        est_vide -> BOOLEEN
        '''
        vide = False
        test = 0
        for x in range(len(self.liste_file)):
            if self.liste_file[x] == None:
                test += 1
        if test == len(self.liste_file):
            vide = True
        
        return vide

    def enfiler(self,element):
        '''
        ajoute un élément dans la file
        ----------
        ajoute le paramètre "element" à la file

        ----------
        enfiler -> VOID
        '''
        if self.est_vide(): # si la liste est vide, on ajoute l'élément dans la première "case" de la file
            self.liste_file[0] = element
            self.index_fin += 1
            # la file étant vide, l'élément a été ajouter à la première case
        else:
            if self.index_fin == self.index_debut: # on vérifie que la liste n'est pas pleine
                # print("la liste est pleine, l'élément ", element, " n'a pas été ajouté")
                return None

            self.liste_file[self.index_fin] = element # on ajoute au niveau de l'index de fin l'élément à ajouter, c'est à dire à la fin de la file
            
            self.index_fin = (self.index_fin+1)%len(self.liste_file) # on décale l'index fin de 1 puisqu'on a rajouté un élément, en vérifiant qu'elle n'est pas pleine

    def defiler(self):
        '''
        retire l'élément de la tête de la file
        ----------
        renvoie l'élément qui a été défilé

        ----------
        defiler -> element
        '''
        if self.est_vide(): # si la file est vide, on ne peut rien défiler
            return None
        
        else:
            a_return = self.liste_file[0] # on sauvegarde l'élément qui sera dépilé, pour le return à la fin
            self.liste_file[self.index_debut] = None # on enlève l'élement qui se trouve dans la première case, c'est-à-dire le premier élément qui a été ajouté
            self.index_debut = (self.index_debut+1)%len(self.liste_file) # on ajoute 1 à l'index de début, tout en vérifiant qu'il ne dépasse pas la taille de la liste
            
            if self.est_vide(): # si la liste est désormais vide, alors on return l'élément qui a été retiré et on arrête
                return a_return

            return a_return
                
    def sommet(self):
        '''
        lit l'élément de la tête de la file sans le retirer
        ----------
        renvoie l'élément qui est sommet de la file.
        Si c'est vide, renvoie None
        ----------
        sommet -> element
        '''
        if self.est_vide():
            print("liste vide, aucun sommet")
            return None # la file étant vide, aucun élément n'est à son sommet
        
        else:
            return self.liste_file[self.index_debut]

    def nombre_elements(self):
        '''
        retourne le nombre d'éléments dans la file
        ----------
        renvoie un int qui correspond au nombre d'élément dans la file

        ----------
        nombre_elements -> entier
        '''
        longueur = 0
        for x in range(len(self.liste_file)):
            if self.liste_file[x] != None:
                longueur += 1

        return longueur

if __name__=="__main__":
    file = File()
    assert file.est_vide() == True # est ce que la liste est vide à ce moment là ? C'est sensé être oui
    for x in range(len(file.liste_file)): # on remplit la file
        file.enfiler(x+1) # attention l'index ne commence pas à 0 pour une meilleure compréhension
    assert file.liste_file == [1,2,3,4,5,6] # on s'assure que la liste de 6 éléments remplit est égal à une suite croissante (on vérifie que la boucle for a bien rempli)
    assert file.enfiler('impossible') == None # puisque la file est pleine, c'est sensé renvoyé None car rien ne peut être ajouté
    file.defiler() # on enlève l'élément 1 de la file
    file.defiler() # on enlève l'élément 2 de la file
    assert file.liste_file == [None,None,3,4,5,6] # on vérifie que les 2 premiers élements de la file on été retiré correctement
    file.enfiler(7) # on enfile 7
    file.defiler() # on enlève l'élément 3 de la file
    assert file.sommet() == 4 # on vérifie que le sommet, c'est-à-dire le prochain élément qui devrait partir est bien 4, car on a enlevé les 3 premiers
    file.enfiler(8) # on enfile 8
    assert file.nombre_elements() == 5 # on vérifie qu'il y a bien 5 élément dans la file : on est parti de 6, enlevé 3 puis rajouté 2, cela donne 5
    print(file.liste_file)