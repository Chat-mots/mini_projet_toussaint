class File :  #classe File de type FIFO

  def __init__(self): # file fonctionnant sans utilisation d'index en attribut et n'ayant pas de taille limite donnée au préalable
    self.file = []

  def enfiler(self,element): # ajout simple d'un élément dans la file sans condition de taille
    self.file.append(element)

  def defiler(self): # suppression du premier élément entré dans la file, méthode qui ne s'applique que s'il y a un élément à supprimer
    if self.est_vide() == False:
      del(self.file[0])

  def est_vide(self): # méthode booléene qui vérifie si la file est vide
    resultat = False
    if self.nombre_elements() == 0 :
      resultat = True
    return resultat

  def sommet(self): # méthode qui retourne le dernier élément entré et qui sera donc retiré le dernier
    return self.file[-1]

  def nombre_elements(self): # méthode qui retourne le nombre d'éléments de la file
    return len(self.file)

  def affiche(self): # méthode qui affiche tous les éléments de la file, ordonnés du permier arrivé au dernier arrivé 
    for i in range (self.nombre_elements()):
      print(self.file[i])

  def test_enfilage(self): # méthode de test, enfile 4 éléments  
    self.enfiler("TRIGHT")
    self.enfiler("TLEFT")
    self.enfiler("D")
    self.enfiler("Q")
  
  def test_defilage(self): # méthode de test, supprime tous les éléments de la file en affichant ceux restants tout en testant la méthode nombre_elements() en affichant le nombre d'éléments restants
    while self.est_vide() != True :
      self.defiler()
      self.affiche()
      print("")
      print("Nombre d'éléments : ",self.nombre_elements())
      print("")

  def test_sommet(self): # méthode de test, affiche clairement l'élément retourné par la méthode sommet()
    print("sommet de la file : ",self.sommet())
    print("")

if __name__ == "__main__" :
  F1 = File()
  F1.test_enfilage()
  F1.affiche()
  print("")
  F1.test_sommet()
  F1.test_defilage()
