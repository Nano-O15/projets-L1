# Projet - "Pile ou Face"

Par OUKHEMANOU Mohand

# DESCRIPTION

Le jeu "Pile ou Face" est un jeu de hasard où le joueur mise sur le résultat d'un lancer de pièce.

Le jeu se déroule de la manière suivante :
    Le joueur mise une certaine somme à chaque tour.
    À chaque tour, le joueur peut choisir de continuer à jouer ou d'arrêter.
Autrement dit, si le joueur décide de continuer, il peut alors remporter ou perdre sa mise.

Le démonstrateur Prolog est utilisé pour simuler les tours de jeu. 
À chaque tour, le joueur peut :
    * continuer de jouer avec ";"
    * ou arrêter de jouer avec "."
Pour tous les tours, la mise est identique. 

# **UTILISATION**

Pour jouer au jeu, suivez ces étapes : 

1. Lancement de l'environnement Prolog :
    Ouvrez votre terminal et entrez la commande suivante pour démarrer l'environnement Prolog : swipl
    Pour quitter l'environnement Prolog, saisissez simplement : halt.

2. Consultation du programme :
    Dans l'environnement Prolog, chargez le programme en entrant la commande suivante : consult('pile_ou_face.pl').

3. Affichage des solutions possibles:
    Utilisez la commande next_etat/2 pour commencer la partie. Les paramètres à fournir sont les suivants :
        Le montant initial dans le pot (total des jetons mis en jeu).
        La mise pour chaque tour.

Exemple d'utilisation de la commande next_etat/2 : 
    next_etat(100,10).