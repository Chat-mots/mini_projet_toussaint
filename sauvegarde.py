class programme:
    def homogenise(self):
        lcaa = liste_chaine_AA()
        cel_lcaa = lcaa.racine
        index = 0
        # cel_courant = commandes_sr[0].racine # cette cellule nous permettra de parcourir la liste de commandes spécial
        # cel_courant = cel_courant.suivant # utiliser pour ne pas avoir comme contenu le contenu de la racine
        for x in commande():
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
        print(lcaa.parcourir())