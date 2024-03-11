#include <stdio.h>
#include <stdlib.h>

#define MIN_CELL 0
#define MAX_CELL 63

void bonus_malus(int *pos_p1, int *pos_p2, int *game_over, int player, int dices_result, int birthday1, int birthday2)
{
    int rng = 0;

    if (*pos_p1 == birthday1 || *pos_p2 == birthday2)
    {
        *game_over = 1;

        printf("Vous etes tombe sur une mauvaise blague ! Vous perdez la partie (https://www.youtube.com/watch?v=BdTgJseXWLM) !\n\n");
    }

    if (*pos_p1 == 7 || *pos_p2 == 7)
    {
        rng = dices_result;

        printf("Vous etes tombe sur un bonus ! Vous avancez de %d cases !\n\n", dices_result);
    }

    if (*pos_p1 == 13 || *pos_p2 == 13)
    {
        rng = -10;

        printf("Vous etes tombe dans un piege ! Vous reculez de 10 cases !\n\n");
    }

    if (*pos_p1 == 21 || *pos_p2 == 21)
    {
        rng = dices_result;

        printf("Vous etes tombe sur un bonus ! Vous avancez de %d cases !\n\n", dices_result);
    }

    if (*pos_p1 == 56 || *pos_p2 == 56)
    {
        printf("Pos1: %d \t Pos2: %d\n", *pos_p1, *pos_p2);
        rng = -55;

        printf("Vous etes tombe dans le puit ! Retournez a la premiere case !\n\n");
    }

    if (rng != 0)
    {
        if (player == 1)
            *pos_p1 += rng;
        else
            *pos_p2 += rng;
    }
}

void change_player(int *player)
{
    if (*player == 1)
        *player = 2;
    else if (*player == 2)
        *player = 1;
}

void check_win(int *game_over, int player, int pos_p1, int pos_p2)
{
    if (pos_p1 >= MAX_CELL || pos_p2 >= MAX_CELL)
    {
        printf("FIN DE JEU !\n\n");
        printf("Le joueur %d a gagne la partie !\n", player);

        *game_over = 1;
    }
}

void change_pos(int *player, int dices_result, int *pos_p1, int *pos_p2)
{
    int move_back;

    if (*player == 1)
        *pos_p1 += dices_result;
    else
        *pos_p2 += dices_result;
    
    if (*pos_p1 > MAX_CELL || *pos_p2 > MAX_CELL)
    {
        if (*player == 1)
        {
            move_back = *pos_p1 - MAX_CELL;
            printf("Vous avez depasse la case finale (%d), vous devez reculer de %d cases\n", *pos_p1, (move_back * 2));
            *pos_p1 -= (move_back * 2);
        }
        else
        {
            move_back = *pos_p2 - MAX_CELL;
            printf("Vous avez depasse la case finale (%d), vous devez reculer de %d cases\n", *pos_p2, (move_back * 2));
            *pos_p2 -= (move_back * 2);
        }

        printf("Pos1: %d \t Pos2: %d\n\n", *pos_p1, *pos_p2);

        return;
    }

    printf("Pos1: %d \t Pos2: %d\n\n", *pos_p1, *pos_p2);
}

int throw_dices(int player)
{
    int dice1, dice2;
    int result;

    dice1 = (rand() % 6) + 1;
    dice2 = (rand() % 6) + 1;

    result = dice1 + dice2;

    printf("Le joueur %d viens de faire un lance de %d, il avance donc de %d cases !\n", player, result, result);
    printf("Le premier de a fait %d et le deuxieme %d !\n\n", dice1, dice2);

    return result;
    
}
