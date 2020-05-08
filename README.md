

#authors :

Asmae MALOULI 18185

Olivia KINNEN 17401

#lancer l'IA : Pour pouvoir jouer en utilisant notre IA il faut lancer dans le terminal la commande suivante : py Avalam.py suivie du port utililsé lors de l'inscription du joueur après avoir lancé le serveur bien sûr et faire l'inscription d'au moins deux joueurs.

#la stratégie est la suivante :

on parcourt la partie "game" du body récupéré, et on construit le dictionnaire a envoyé "action", la clé "from" contient la position actuelle et "to" contient la position à atteindre (en regardant où on peut se déplacer ) cette action sera acceptée si elle répond aux règles du jeu; pour ça on a définit une méthode IsItGood.

le déplacement se fait grâce à deux listes [-1,0,1](vu qu'on peut se déplacer que sur 9 places autour de la position actuelle, suivant x: gauche, pas de mouvement et droite; et suivant y: bas, pas de mouvement et haut) en ajoutant chaque fois un de ses éléments aux coordonnés de la place actuelle.

le planA de notre ia est de faire un coup parfait pour cela on a construit une méthode IsPerfect qui check si le coup envoyé va emmener vers un état ou la longueur du tour sera égale à 5 ET s'assure que le pion de dessus sera le notre.

le planB alors sera d'envoyer un coup qui respecte les règles seulement  qui  est  vérifié toujours grâce à IsItGood.

on a aussi essayé de ne pas jouer en ordre( du haut vers le bas et droite vers la gauche )en utilisant le module random mais cela genérait des BadMoves...