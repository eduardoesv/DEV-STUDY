#include <stdio.h>

int main() {

    int n, i, j;
    n = 3;

    printf("Digite a matriz:\n");

    int matriz[n][n];

    for (i = 0; i <= n; i++) {
        for (j = 0; j <= n; j++) {        
            printf("Elemento [%d,%d]: ", i, j);
            scanf("%d", &matriz[i][j]);
        }
    }

    
    return 0;
}