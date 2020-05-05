# AvalamAi
la stratégie est la suivante : 
on parcourt la partie "game" du body récupéré, et on construit  le dictionnaire a envoyé "action", la clé "from" contient la position 
actuelle et "to" contient la position a atteindre si l'action repond aux règles du jeu; pour ça on a definit une méthode IsItGood.
le deplacement se fait grace a deux  listes [-1,0,1] ( gauche, pas de mouvement,droite) et (bas,pas de mouvement, haut).
le planA de notre ia est de faire un coup parfait pour cela on a construit une méthod IsPerfect qui check si le coup envoyé va emmener 
vers un état ou la longueur du tour sera égale à 5 ET s'assure que le pion de dessus sera le notre.
le planB alors sera d'envoyer un coup qui respect les regles 
on a aussi essayé de ne pas jouer en ordre( du haut vers  le bas et droite vers la gauche ) mais ca genère des BadMoves...

