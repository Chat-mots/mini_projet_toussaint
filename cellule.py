class cellule:
    """
    classe représentant une cellule dans une liste
    ---
    ATTRIBUTS :
    prec => adresse de cellule ou None : Adresse de la cellule précédente. None par défaut
    suivant => adresse de cellule ou None : Adresse de la cellule suivante. None par défaut
    contenu => N'importe quel type de donnée : Contenu de la cellule. None par défaut
    ---
    METHODES :
    modifier(contenu): Modifie le contenu de la valeur
    afficher : Affiche les attributs actuels de la cellule
    """

    def __init__(self) -> None:
        self.prec = None
        self.suivant = None
        self.contenu = None

    def modifier(self,contenu):
        """
        permet de modifier le contenu d'une cellule
        ---
        contenu : nouveau contenu de la cellule
        """
        self.contenu = contenu

    def afficher(self):
        """
        affiche "prec", "suivant" et "contenu" de la cellule
        """
        print("précedent : ", self.prec)
        print("suivant : ", self.suivant)
        print("contenu : ", self.contenu)

if __name__ == "__main__":
    cel = cellule()
    cel.modifier("valeur")
    print(cel.contenu)
    cel.afficher()