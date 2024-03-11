#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "../headers/fonctions.h"

#define MIN_CELL 0

int main()
{
    int player = 1, pos_p1 = MIN_CELL, pos_p2 = MIN_CELL;
    int game_over = 0;
    int dices_result;
    int choice;
    int birthday1, birthday2;

    printf("Joueur 1 entrer votre jour d'anniversaire : ");
    scanf("%d", &birthday1);

    printf("Joueur 2 entrer votre jour d'anniversaire : ");
    scanf("%d", &birthday2);
    
    printf("\n");

    srand(time(NULL));

    printf("Le joueur 1 commence la partie.\n\n");

    while (!game_over)
    {
        check_win(&game_over, player, pos_p1, pos_p2);
        if (game_over)
            continue;
        
        printf("C'est au tour du joueur %d ! Pour lancer le de entrez 1 (pour quitter la partie entrez une autre valeur) : ", player);
        scanf("%d", &choice);
        printf("\n");

        if (choice != 1)
        {
            printf("Vous avez choisi de quitter la partie.\n");
            break;
        }

        dices_result = throw_dices(player);

        change_pos(&player, dices_result, &pos_p1, &pos_p2);
        bonus_malus(&pos_p1, &pos_p2, &game_over, player, dices_result, birthday1, birthday2);

        check_win(&game_over, player, pos_p1, pos_p2);
        if (game_over)
            continue;

        change_player(&player);
    }

    return EXIT_SUCCESS;
}