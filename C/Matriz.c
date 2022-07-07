#include <stdio.h>

int main() {

    int n, i, j, produto;
    n = 3;
    produto = 0;

    printf("Digite a matriz:\n");

    int matriz[n][n];

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {        
            printf("Elemento [%d,%d]: ", i, j);
            scanf("%d", &matriz[i][j]);
        }
    }
    
    printf("\nResultado da matriz:\n");

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {        
            produto = matriz[i][j] * 5;
            printf("%d ", produto);            
        }
        printf("\n");
    }
    
    return 0;
}