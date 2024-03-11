# Projet - "Sudoku Solver (4x4)"

Par OUKHEMANOU Mohand

# DESCRIPTION

Ce projet est un résolveur de sudoku pour des grilles de dimension 4x4.

# **UTILISATION**

Pour utiliser le résolveur de sudoku, suivez ces étapes :

1. Lancement de l'environnement Prolog :
    Ouvrez votre terminal et entrez la commande suivante pour démarrer l'environnement Prolog : swipl
    Pour quitter l'environnement Prolog, saisissez simplement : halt.

2. Consultation du programme :
    Dans l'environnement Prolog, chargez le programme en entrant la commande suivante : consult('pile_ou_face.pl').

3. Affichage des solutions possibles:
Il existe plusieurs prédicats pour afficher les solutions :
        Utilisez la commande sudoku/1 pour obtenir une solution directe. 
        Le paramètre à fournir est la grille du sudoku sous forme de liste.
        Exemple d'utilisation de la commande sudoku/1 : 
            sudoku([1,,3,4,A,B,C,D,2,3,4,1,E,F,G,H]).
        
        Utilisez la commande sudoku2/1 pour obtenir une solution en utilisant la méthode "générer-tester". 
        Le paramètre à fournir est la grille du sudoku sous forme de liste.
        Dans cette solution, les valeurs sont représentées par des puissances de 2 (1 représenté par 2^0, 2 par 2^1, 3 par 2^2 et 4 par 2^3). 
        Le prédicat nombre retourne vrai si la valeur passée est égale à 1, 2, 4 ou 8
        Le prédicat sudoku vérifie les contraintes du sudoku 4x4. :
            *** les valeurs vérifient le prédicat nombre
            *** la somme des valeurs en ligne est égale à 15 
            *** la somme des valeurs en colonne est égale à 15 
            *** la somme des valeurs dans les blocks est égale à 15.
        Exemple d'utilisation de la commande sudoku2/1 : 
            sudoku2([1,2,4,8,A,B,C,D,2,4,8,1,E,F,G,H]).

        Utilisez la commande all_sol_sudoku2/1 pour obtenir toutes les solutions possibles de manière non interactive. 
        Le paramètre à fournir est la grille du sudoku sous forme de liste. 
        Le prédicat all_sol_sudoku2 résout le sudoku et affiche toutes les solutions en ligne, numérotées.
        Exemple d'utilisation de la commande all_sol_sudoku2/1 : 
            all_sol_sudoku2([1,2,4,8,A,B,C,D,2,4,8,1,E,F,G,H]).