class File :

  def __init__(self):
    self.file = []

  def enfiler(self,element):
    self.file.append(element)

  def defiler(self):
    if self.est_vide() == False:
      del(self.file[0])

  def est_vide(self):
    resultat = False
    if self.nombre_elements() == 0 :
      resultat = True
    return resultat

  def sommet(self):
    return self.file[-1]

  def nombre_elements(self):
    return len(self.file)

  def affiche(self):
    for i in range (self.nombre_elements()):
      print(self.file[i])

  def test_enfilage(self):
    self.enfiler("INIT")
    self.enfiler("TLEFT")
    self.enfiler("D")
    self.enfiler("Q")
  
  def test_defilage(self):
    while self.est_vide() != True :
      self.defiler()
      self.affiche()
      print("")
      print("Nombre d'éléments : ",self.nombre_elements())
      print("")

  def test_sommet(self):
    print("sommet de la file : ",self.sommet())
    print("")

if __name__ == "__main__" :
  F1 = File()
  F1.test_enfilage()
  F1.affiche()
  print("")
  F1.test_sommet()
  F1.test_defilage()
