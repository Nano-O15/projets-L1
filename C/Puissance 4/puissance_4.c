#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define width 6
#define height 7

void display_grid(int grid[width][height]);
int check_if_power4(int grid[width][height], int player_playing);

void display_grid(int grid[width][height])
{
    int i, j; /* utilises pour les boucles */

    printf("Voici la Grille Actuelle:\n\n");

    printf("A  B  C  D  E  F  G\n");

    for (i = 0; i < width; i++) /* lignes */
    {
        for (j = 0; j < height; j++) /* colonnes */
        {
            printf("%d  ", grid[i][j]);
        }

        printf("\n");
    }

    printf("\n");
}

int check_if_power4(int grid[width][height], int player_playing)
{
    int game_over = 0; /* la valeur que l'on va retourner a la fin: soit 0 soit 1 */
    char win_type[15]; /* chaine de characteres indiquant le type d'alignement */

    int i, j; /* utilises pour les boucles */

    for (i = 0; i < width; i++)
    {
        for (j = 0; j < height - 3; j++)
        {
            // Victoire Horizontale
            if (grid[i][j] == player_playing && grid[i][j] == grid[i][j + 1] && grid[i][j] == grid[i][j + 2] && grid[i][j] == grid[i][j + 3])
            {
                strcpy(win_type, "Horizontale");
                game_over = 1;
            }
        }
    }

    for (i = 0; i < width - 3; i++)
    {
        for (j = 0; j < height; j++)
        {
            // Victoire Verticale
            if (grid[i][j] == player_playing && grid[i][j] == grid[i + 1][j] && grid[i][j] == grid[i + 2][j] && grid[i][j] == grid[i + 3][j])
            {
                strcpy(win_type, "Verticale");
                game_over = 1;
            }
        }
    }

    for (i = 0; i < width - 3; i++)
    {
        for (j = 0; j < height - 3; j++)
        {
            // Victoire Diagonale Droite
            if (grid[i][j] != 0 && grid[i][j] == grid[i + 1][j + 1] && grid[i][j] == grid[i + 2][j + 2] && grid[i][j] == grid[i + 3][j + 3])
            {
                strcpy(win_type, "Diagonale");
                game_over = 1;
            }
        }
    }

    for (i = 0; i < width - 3; i++)
    {
        for (j = 0; j < height - 3; j++)
        {
            // Victoire Diagonale Gauche
            if (grid[i][j] != 0 && grid[i][j] == grid[i + 1][j - 1] && grid[i][j] == grid[i + 2][j - 2] && grid[i][j] == grid[i + 3][j - 3])
            {
                strcpy(win_type, "Diagonale");
                game_over = 1;
            }
        }
    }

    if (game_over == 1) /*si player_playing gagne alors affiche la grille et un peu de texte final*/
    {
        system("clear");
        display_grid(grid);
        printf("**** Joueur %d a Gagne en %s ****\n\n", player_playing, win_type);
        printf("FIN DU JEU\n\n");
    }

    return game_over; /* on retourne 0 ou 1 */
}

int main()
{
    /* grille du jeu en width x height */
    int grid[width][height] = {
        {0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0},
    }; /* matrice width x height, rien de plus simple */

    int game_over = 0, played = 0, player_playing = 1;
    int retry = 0;
    int i = 0; /* pour les boucles for */

    /*
        - game_over sert a rester dans la boucle tant que cette variable est egale a 0
        - played sert a verifier que le jouer a deja jouer, dans quel cas on va plus faire
          de verification dans la boucle (on skip tout dans la boucle for avec continue)
        - player_playing designe le jouer actuel (1 ou 2), c'est ce que l'on place dans la grille
    */

    char column; /* valeur que l'on scanne -> A B C D E F ou a b c d e f */

    while (!game_over)
    {
        display_grid(grid); /* on affiche la grille */

        printf("C'est au tour du joueur %d\n", player_playing);
        printf("Entrez une colonne: ");
        scanf(" %c", &column); /* on affecte la valeur scannee a column */

        printf("\n");

        /*
            En fonction de ce que l'utilisateur entre (donc A,B,C ou a,b,c etc)
            on attribue l'index de la ligne de la matrice. Donc si le joueur entre
            A (ou a), il veut placer son jeton dans la colonne 1
            (qui est l'index 0 dans un tableau en programmation)
        */

        if (column == 'A' || column == 'a')
        {
            column = 0;
            retry = 0;
        }
        else if (column == 'B' || column == 'b')
        {
            column = 1;
            retry = 0;
        }
        else if (column == 'C' || column == 'c')
        {
            column = 2;
            retry = 0;
        }
        else if (column == 'D' || column == 'd')
        {
            column = 3;
            retry = 0;
        }
        else if (column == 'E' || column == 'e')
        {
            column = 4;
            retry = 0;
        }
        else if (column == 'F' || column == 'f')
        {
            column = 5;
            retry = 0;
        }
        else if (column == 'G' || column == 'g')
        {
            column = 7;
            retry = 0;
        }
        else
        {
            printf("Cette colonne n'existe pas, rejoue !\n\n");
            retry = 1;
        }

        /*
            Ici on ne fait qu'une seule boucle tout simplement parce que l'on a pas
            besoin de rechercher toutes les colonnes, logique non ? Puisque la colonne
            qui nous interesse nous l'avons deja (designe par l'utilisateur), affectee
            a la variable column
        */

        for (i = 0; i < width; i++) /* les lignes */
        {

            /*
                si la colonne de la derniere ligne est vide (egale a 0) alors on peut placer ici.
                played = 1; sera pris en compte dans le prochain test if qui va donc nous permettre
                d'ignorer toutes les prochaines iterations (tour de boucle).
            */
            if (grid[5][(int)column] == 0)
            {
                grid[5][(int)column] = player_playing;
                played = 1;
            }

            if (played == 1)
                continue; /* continue veut dire: faire passer le tour, donc ignorer tout ce qui suit apres ce block */

            /*
                Si la colonne n'est pas vide
            */
            if (grid[i][(int)column] != 0)
            {
                /*
                  Et donc si la colonne juste au dessus (i-1) est vide
                  on peut placer le jeton du joueur
                */
                if (grid[i - 1][(int)column] == 0)
                {
                    grid[i - 1][(int)column] = player_playing;
                }
            }
        }

        /*
            On affecte a game_over ce que la fonction check_if_power4 retourne (soit 0 soit 1)
            si la valeur = 1, le jeu s'arrete ici.
        */

        game_over = check_if_power4(grid, player_playing);

        /*
            On change de joueur a chaque tour biensur.
        */

        if (retry == 0)
        {
            if (player_playing == 1)
                player_playing = 2;
            else
                player_playing = 1;
        }

        if (retry == 1)
        {
            if (player_playing == 1)
                player_playing = 1;
            else
                player_playing = 2;
        }

        /*
            Puisque le tour est fini, on dit que le nouveau tour n'a pas encore ete joue evidemment.
            On reset played quoi
        */
        played = 0;
    }
}
