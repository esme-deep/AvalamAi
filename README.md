

#authors : 

Asmae MALOULI 18185

Olivia KINNEN 17401


#lancer l'IA : 
Pour pouvoir jouer en utilisant notre IA il faut lancer dans le terminal la commande suivante :
py Avalam.py suivi du port utililsé lors de l'inscription du joueur  apres avoir lancer le serveur biensur 
et faire l'inscription d'au moins deux joueurs. 







#la stratégie est la suivante : 

on parcourt la partie "game" du body récupéré, et on construit  le dictionnaire a envoyé "action", la clé "from" contient la position 
actuelle et "to" contient la position a atteindre(en regardant ou on peut se déplacer ) cette action sera accepté s'elle repond aux règles du jeu; pour ça on a definit une méthode IsItGood.

le deplacement se fait grace a deux  listes [-1,0,1](vu qu'on peut se déplacer sur 9 places autour de la position actuelle, suivant x: gauche, pas de mouvementet droite et suivant y: bas,   pas de mouvement et  haut) en ajoutant chaque fois un de ses elements au coordonnés de la place actuelle.

le planA de notre ia est de faire un coup parfait pour cela on a construit une méthod IsPerfect qui check si le coup envoyé va emmener 
vers un état ou la longueur du tour sera égale à 5 ET s'assure que le pion de dessus sera le notre.

le planB alors sera d'envoyer un coup qui respect les regles qui est verifié toujours grace a IsItGood.

on a aussi essayé de ne pas jouer en ordre( du haut vers  le bas et droite vers la gauche ) mais cela genèrait des BadMoves...





