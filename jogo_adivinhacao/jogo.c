#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int numero_secreto, palpite, tentativas = 0;

    // random number 1 to 100
    srand(time(NULL));
    numero_secreto = rand() % 100 + 1;

    printf("Bem-vindo ao Jogo de Adivinhação!\n");
    printf("Tente adivinhar o número secreto entre 1 e 100.\n");

    while (1) {
        printf("Digite seu palpite: ");
        if (scanf("%d", &palpite) != 1) {
            printf("Entrada inválida. Digite um número.\n");
            while (getchar() != '\n'); // limpa buffer
            continue;
        }

        tentativas++;

        if (palpite < numero_secreto) {
            printf("O número secreto é MAIOR.\n");
        } else if (palpite > numero_secreto) {
            printf("O número secreto é MENOR.\n");
        } else {
            printf("Parabéns! Você acertou em %d tentativas.\n", tentativas);
            break;
        }
    }

    return 0;
}

