class cellule:

    def __init__(self) -> None:
        self.prec = None
        self.suivant = None
        self.contenu = None

    def modifier(self,contenu):
        self.contenu = contenu

    def afficher(self):
        print("précedent : ", self.prec)
        print("suivant : ", self.suivant)
        print("contenu : ", self.contenu)

if __name__ == "__main__":
    cel = cellule()
    cel.modifier("valeur")
    print(cel.contenu)
    cel.afficher()