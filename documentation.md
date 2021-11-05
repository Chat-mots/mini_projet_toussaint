<h1> Documentation du projet NSI pour la Toussaint </h1>

<h2> Classe PILE </h3>
TAD dont le fonctionnement est l'empilement/depilement : L'element entre en dernier et le premier à sortir
<h4> Attributs :</h4>
<ul>
    <li> <strong>p</strong> => LISTE : contenu de la pile
    <li> <strong>nbr_elements</strong> => INT : Le nombre d'éléments dans la pile
</ul>
<h4> Méthodes : </h4>
<ul>
    <li><strong> empiler (element)</strong> : Ajoutes un élément à la pile et incrémente de 1 nbr_elements
    <li><strong> est_vide </strong> : Renvoie True si la liste ne contient pas d'éléments ou False le cas contraire
    <li>  <strong> depiler </strong> : Renvoie l'élément en haut de la pile et le retire de la pile
    <li> <strong> dernier </strong> : Renvoie l'élément en haut de la pile sans le supprimer
    <li> <strong> visualiser </strong> : Affiche la pile en la dépilant élément par élément
</ul>
<h2> Classe LISTE_CHAINEE_AA </h2>
<h4> Attributs : </h4>
<ul>
    <li><strong>racine</strong> => Instance de la classe cellule : La première cellule de la liste, généralement vide et permettant le parcours de la liste
</ul>
<h4> Méthodes : </h4>
<ul>
    <li><strong>est_vide</strong> : Renvoie True si la liste ne contient pas de cellule hormis racine, et False inversement
    <li><strong>ajouter(c)</strong> : Ajoute une cellule avec comme contenu c à la fin de la liste et renvoie l'adresse de la cellule nouvellement crée
    <li><strong> inserer(contenu,cellule => adresse d'une cellule)</strong>: Insère une nouvelle cellule avec comme contenu contenu après la cellule cellule et renvoie l'adresse de la cellule nouvellement crée. Vériies aussi que cellule existe dans la liste chaînée, et le cas contraire renvoit un message d'erreur.
    <li><strong> parcourir</strong> : Parcourt la liste en affichant chaque contenu de chaque cellule
    <li> <strong> trouver (contenu) </strong> : Parcourt la liste jusqu'à trouver la première cellule avec comme contenu le paramètre donné, et renvoie l'adresse de la première cellule ainsi trouvée
    <li><strong> supprimer (cellule_sup => adresse d'une cellule) </strong> : Parcourt la liste jusqu'à trouver la première cellule avec comme adresse cellule_sup et supprimes la cellule trouvée ainsi
</ul>
<h2> Classe CELLULE </h2>
<h4> Attributs : </h4>
<ul>
    <li><strong>prec</strong> => adresse de cellule ou None : Adresse de la cellule précédente. None par défaut
    <li><strong>suivant</strong> => adresse de cellule ou None : Adresse de la cellule suivante. None par défaut
    <li><strong>contenu</strong> => N'importe quel type de donnée : Contenu de la cellule. None par défaut
</ul>
<h4> Méthodes : </h4>
<ul>
    <li><strong>modifier(contenu)</strong> : Modifie le contenu de la valeur
    <li><strong>afficher</strong> : Affiche les attributs actuels de la cellule
</ul>
<h2> Classe FILE (t) </h2>
<h4> Attributs : </h4>
<ul>
    <li><strong> file </strong> => liste : Liste remplie de None de taille t
    <li><strong> tmax </strong> => int : Taille maximale de la file (égale à t)
    <li><strong> index_debut </strong> => int : Index de sortie de la file. 0 à l'initialisation.
    <li><strong> index_fin </strong> => int : Index d'entrée de la file. 0 à l'initialisation.
    <li><strong> nbr_elements </strong> => int : Nombre d'éléments actuels de la file. 0 à l'initialisation
</ul>
<h4> Méthodes : </h4>
<ul>
    <li><strong>est_vide</strong> : Renvoie True si le nbr_elements = 0, renvoie False dans le cas contraire
    <li><strong>enfiler (element)</strong> : Ajoute un élément dans la liste, à l'index de fin, puis incrémentes de 1 l'index de fin.
    <li><strong> defiler </strong> : Renvoie l'élément à l'index de début, puis remplace l'élément à l'index de début par None. Incrémentes ensuite l'index de début de 1.
    <li><strong> sommet </strong> : Renvoie l'élément à l'index de début, sans le supprimer ni incrémenter l'index de début.
    <li><strong>nombre_elements</strong> : Renvoie nbr_elements
<h2> Classe PROGRAMME </h2>
<h4> Attributs : </h4>
    <li><strong> p </strong> => instance de la classe pile : Pile du programme
    <li><strong> lcaa </strong> => instance de la classe lcaa : liste chaînéee avant arrière du programme
    <li><strong> file </strong> => Au début None, plus tard une instance de la classe file, de taille égale au nombre de l'élément de lcaa : file du programme
<h4> Méthodes : </h4>
<ul>
    <li><strong> gestion_commandes </strong> : Boucle while qui récupère les commandes de l'utilisateur, et vérifie chaque commande entrée par l'utilisateur afin de vérifier qu'elle existe bien, puis l'empile dans p si c'est une commande base, ou l'exécute si c'est une commande_prog. Retourne une pile.
    <li><strong> import_sr </strong> : Récupères les commandes sr de sr.txt, les ajoutes aux commandes de base du programme, et ajoutes leur lcaa dans commandes_sr du fichier config.py. Retourne des lcaa pour chaque subroutines.
    <li><strong>homogenise</strong> : Récupères la pile du programme en faisant une deepcopy de cette dernière, puis convertit la copie en liste chaînée avant arrière, en insérant correctement chaque cellule composant les commandes sr (il ne faut pas insérer les racines !). Retourne une file.
    <li><strong>transfert_file</strong> : Récupères la lcaa du programme en la deepcopiant, récupère le nombre d'éléments de la lcaa en la parcourant (ne pas compter la racine), puis crée une file (en écrasant self.file du programme) de la taille du nombre d'éléments de la lcaa. Convertit ensuite chaque élément non-racine de la lcaa en éléments de la file.
    <li><strong>executer</strong> : Affiches la file du programme
</ul>
<h2> A FAIRE </h2>
Chaque classe devra être vérifiée : Qu'elle respecte bien la documentation (bon noms d'attributs/méthodes et qu'elle fonctionne comme indiqué) et qu'elle possède son jeu de test (avec utilisation de assert et de la vérification du __name__ == "__main__").
Les classes sont :
<ul>
    <li>La classe <strong> pile </strong> (pas d'élève défini)
    <li> La classe <strong> lcaa </strong> (Léandre)
    <li> La classe <strong> file </strong> (pas d'élève défini)
    <li> La classe <strong> programme </strong> (Victor)
</ul>
Egalement, un dernier élèvre devra s'occuper de la conformité pep8 de CHAQUE classe (pas d'élève défini).

