#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

// Definindo tamanho da lista para simplificar alocação
#define TAMANHO_ARRAY 1000000 

typedef struct carrinho {
    double preco;
    int quantidade;
} carrinho_t, *carrinho_p;

double calculo_loop(carrinho_p carrinhos, int tamanho) {
    double total = 0;
    for (int i = 0; i < tamanho; i++) {
        total += carrinhos[i].preco * carrinhos[i].quantidade;
    }
    return total/tamanho;
}

int main(int argc, char* argv[]) {
    carrinho_p carrinhos = malloc(TAMANHO_ARRAY * sizeof(carrinho_t));
    for (int i = 0; i < TAMANHO_ARRAY; i++) {
        double preco;
        int quantidade;
        scanf("%lf\t%d", &preco, &quantidade);
        carrinhos[i].preco = preco;
        carrinhos[i].quantidade = quantidade;
    }

    double t0, t1;
    struct timeval timeval0, timeval1;

    gettimeofday(&timeval0, NULL);
    double media = calculo_loop(carrinhos, TAMANHO_ARRAY);
    gettimeofday(&timeval1, NULL);

    t0 = (double)timeval0.tv_sec + (double)timeval0.tv_usec / 1000000;
    t1 = (double)timeval1.tv_sec + (double)timeval1.tv_usec / 1000000;

    printf("Tempo Calculo: %lfs\n", (t1 - t0));
    printf("%lf\n", media);
    free(carrinhos);
    return 0;
}