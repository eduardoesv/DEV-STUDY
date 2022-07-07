#include <stdio.h>

int num, status = 0;

int verificacao (int num){ //FUNCAO RETORNA 1 PARA NUMEROS PARES E 0 PARA NUMEROS IMPARES
    if(num%2==0){
        status = 1;
    }else{
        status = 0;
    }
}

int main(){

    int valInicial, valFinal, contagemPares, i;

    printf("Digite o valor inicial: \n");
    scanf("%d", &valInicial);

    printf("Digite o valor final: \n");
    scanf("%d", &valFinal);

    while (valFinal <= valInicial) { //ESTRUTURA PARA EVITAR QUE O NUMERO FINAL SEJA INFERIOR QUE O INICAL
        printf("Digite um valor final maior que o valor inicial: \n");
        scanf("%d", &valFinal);
    }
    
    printf("\n");

    for (i = valInicial; i <= valFinal; i++) {

        verificacao(i); //EXECUTA A FUNCAO RETORNANDO O RESULTADO DA CHECAGEM

        if (status == 1) {
            printf("%d é um numero par\n", i);
            contagemPares++;
        }else{
            printf("%d é um numero impar\n", i);
        }
    }
    
    printf("\nTotal de numeros pares: %d", contagemPares);

    return 0;
}