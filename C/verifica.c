#include <stdio.h>

int n1,n2, contador, qtd_pares = 0;
	
		
int verifica (int n1, int n2){//FUNCAO 
	
		while(n2 <= n1){//NAO PERMMITE CONTAGEM NEGATIVA
			printf("Digite um valor valido maior que o valor incial %d", n1);
			printf("\nDigite o numero final\n");
			scanf("%d", &n2);
	}
	
		for(contador = n1; contador <= n2; contador++){//VALIDADOR DE NUMEROS PARES E IMPARES
			if(contador%2==0){
			printf("O numero %d e PAR!\n", contador);
			qtd_pares++;
		}else{
			printf("O numero %d e IMPAR!\n", contador);
		}
	}
}
  
	
int main(){
	
	printf("*****************");
	printf("\n**Bem vindo ao nosso verificador de numeros**\n");
	printf("***** Pares e Impares ****\n");
	printf("*****************");
	
	
	int inicial, final;
	
	printf("\nDigite o numero inicial\n");
	scanf("%d",&inicial);
	
	printf("\nDigite o numero final\n");
	scanf("\n%d",&final);
		
	
 	verifica(inicial,final); //CHAMA FUNÇÃO DE VERIFICAÇÃO DE NUMEROS PARES E IMPARES
	

	
	printf("\nA quantidade de numeros pares e %d", qtd_pares);
	return(0);
	
}