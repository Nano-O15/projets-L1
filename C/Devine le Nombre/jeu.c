#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int inscription(char user[20], char password[20]);

int authentification(char user[20], char password[20]);

int devine(char user[20]);

int get_score(char user[20], int score);

int inscription(char user[20], char password[20])
{
    FILE *file = NULL;

    file = fopen("user.txt", "a");

    if (file != NULL)
    {
        fputs(user, file);

        fputs(password, file);
        
        fclose(file);
    }

    else
    {
        printf("Erreur ! Le fichier n'existe pas !\n");
    }

    printf("Vous etes maintenant inscrit !\n\n");

    devine(user);

    return 0;
}

int authentification(char user[20], char password[20])
{
    FILE *file = NULL;
    char string[20];

    file = fopen("user.txt", "r");

    if (file != NULL)
    {
        while (fgets(string, 20, file) != NULL)
        {
            if ((strcmp(string,user) == 0))
            {
                printf("\n");
                printf("Le nom d'utilisateur est reconnu !\n\n");

                while (fgets(string, 20, file) != NULL)
                {
                    if ((strcmp(string, password) == 0))
                    {
                        printf("Le mot de passe de l'utilisateur est reconnu !\n\n");
                        printf("Bienvenue, vous avez reussi a vous authentifier !\n\n");
                        devine(user);
                        //break;
                    }

                    else
                    {
                        printf("Erreur, mot de passe incorrect !\n\n");
                        break;
                    }
                }

                break;
            }
        }

        fclose(file);
    }

    else
    {
        printf("Erreur ! Le fichier n'existe pas !\n");
    }

    return 0;
}

int devine(char user[20])
{
    int max = 100;
    int proposition;
    int nb_devine;
    int coups = 10;
    int play_again;
    int score;

    srand(time(NULL));
    printf("Vous allez maintenant jouer a 'Devine le Nombre' !\n");
    printf("Vous n'avez le droit qu'a 10 tentatives pour trouver la bonne reponse !\n\n");
    nb_devine = rand() % max;

    for(int i = 0; i < coups; i++)
    {
        printf("Entrez un nombre entre 0 et %d.\n", max);
        scanf("%d", &proposition);

        if(nb_devine == proposition)
        {
            printf("Bravo, vous avez trouvé en %d coups !\n\n", i+1);
            score = i+1;
            printf("Score = %d\n\n", score);
            get_score(user, score);
            printf("Voulez-vous rejouer ? (1 ou 2)\n");
            scanf("%d", &play_again);

            if(play_again == 1)
            {
                devine(user);
            }

            if(play_again == 2)
            {
                exit(2);
            }

            else
            {
                printf("Erreur, mauvais choix de reponse !\n");
            }
        }

        if(nb_devine < proposition)
        {
            printf("C'est plus Petit !\n\n");
        }

        else
        {
            printf("C'est plus Grand !\n\n");
        }

        if(i+1 == coups)
        {
            if(nb_devine != proposition)
            {
                printf("Perdu ! C'est dommage vous n'avez pas trouve la bonne reponse !\n\n");
                printf("Voulez-vous rejouer ? (1 ou 2)\n");
                scanf("%d", &play_again);

                if(play_again == 1)
                {
                    devine(user);
                }

                if(play_again == 2)
                {
                    exit(2);
                }

                else
                {
                    printf("Erreur, mauvais choix de reponse !\n");
                }
            }
        } 
    }

    return 0;
}

int get_score(char user[20], int score)
{
    FILE *file = NULL;

    file = fopen("score.txt", "a");

    char score_str[4];

    sprintf(score_str, "%d", score);

    if (file != NULL)
    {
        fputs(user, file);

        strcat(score_str, "\n");
        fputs(score_str, file);
        
        fclose(file);
    }

    else
    {
        printf("Erreur ! Le fichier n'existe pas !\n");
    }

    return 0;
}

int main()
{
    char user[20];
    char password[20];
    int choice;

    printf("Si vous voulez jouer veuillez vous inscrire ou vous authentifier !\n");
    printf("Pour vous inscrire : 1. Pour vous authentifier : 2.\n");
    scanf("%d", &choice);

    if (choice == 1)
    {
        printf("Veuillez saisir un nom d'utilisateur (18 caracteres max) : \n");
        scanf("%s", user);
        strcat(user, "\n");
        printf("Votre nom d'utilisateur est : %s\n", user);

        printf("Veuillez saisir un mot de passe (18 caracteres max) : \n");
        scanf("%s", password);
        strcat(password, "\n");
        printf("Votre mot de passe est : %s\n", password);

        inscription(user, password);
    }

    if (choice == 2)
    {
        printf("Veuillez saisir votre nom d'utilisateur : \n");
        scanf("%s", user);
        strcat(user, "\n");

        printf("Veuillez saisir votre mot de passe : \n");
        scanf("%s", password);
        strcat(password, "\n");

        authentification(user, password);
    }

    return 0;
} 