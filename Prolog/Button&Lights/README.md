# Projet - "Buttons and Lights"

Par OUKHEMANOU Mohand

# DESCRIPTION

Le jeu "Buttons and Lights" est un jeu où le but est d'allumer toutes les lampes en utilisant un ensemble d'actions spécifiques.

## Exemple

Pour illustrer le fonctionnement du jeu, considérons un exemple avec 3 lampes nommées A, B et C :
    L'action 1 allume la première lampe.
    L'action 2 échange les valeurs de la première et de la deuxième lampe.
    L'action 3 échange les valeurs de la deuxième et de la troisième lampe.

Si nous sommes dans un état où la première lampe est allumée, la deuxième lampe est allumée et la troisième lampe est éteinte :
    En effectuant l'action 1, l'état actuel reste inchangé.
    En effectuant l'action 3, l'état actuel devient : la première lampe est allumée, la deuxième lampe est éteinte et la troisième lampe est allumée.

# PRÉ-REQUIS

Avant de pouvoir exécuter le jeu, assurez-vous d'avoir Prolog et l'environnement SWI-Prolog installés sur votre machine. 
Vous pouvez les télécharger depuis le site officiel :  https://www.swi-prolog.org/download/stable

# **UTILISATION**

Pour jouer au jeu, suivez ces étapes : 

1. Lancement de l'environnement Prolog :
    Ouvrez votre terminal et entrez la commande suivante pour démarrer l'environnement Prolog : 
        swipl
    Pour quitter l'environnement Prolog, saisissez simplement : 
        halt.

2. Consultation du programme :
    Dans l'environnement Prolog, chargez le programme en entrant la commande suivante : consult('buttons_and_lights3.pl').

3. Affichage des solutions possibles:
    Utilisez la commande jouer/4 pour afficher les solutions possibles pour une configuration donnée. Les paramètres à fournir sont les suivants :
        État de la lampe 1 (0 pour éteinte, 1 pour allumée)
        État de la lampe 2
        État de la lampe 3
        Nombre maximal de coups par solution.

Exemple d'utilisation de la commande jouer/4 : 
    jouer(0, 0, 0, 6).