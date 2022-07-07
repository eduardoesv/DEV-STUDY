Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/02/2022
Var
 a : vetor [0..9, 0..9] de real
 x, y, i, j, l, c : inteiro
 z1, z2, z3 : real
 maior : vetor [0..9] de inteiro

Inicio
      escreval("Qual a ordem da matriz? ")
      leia(x)

      escreval("Digite os valores da matriz A")
      para i de 0 ate x-1 faca
           para j de 0 ate x-1 faca
                escreva("Elemento [", i, ",", j, "] : ")
                leia(a[i,j])
           fimpara
      fimpara
      
      escreval

      z1 <- 0
      para i de 0 ate x-1 faca
        para j de 0 ate x-1 faca
           se a[i,j] > 0 entao
             z1 <- z1 + a[i,j]
           fimse
        fimpara
      fimpara
      escreval("SOMA DOS POSITIVOS: ", z1:2:1)
      escreval
      
      escreva("Escolha uma linha: ")
      leia(l)
      escreva("LINHA ESCOLHIDA: ")
      para i de 0 ate x-1 faca
           escreva(a[l,i]:2:1, " ")
      fimpara
      escreval
      escreval
      
      escreva("Escolha uma coluna: ")
      leia(c)
      escreva("COLUNA ESCOLHIDA: ")
      para i de 0 ate x-1 faca
           escreva(a[i,c]:2:1, " ")
      fimpara
      escreval
      escreval
      
      escreva("DIAGONAL PRINCIPAL: ")
      para i de 0 ate x-1 faca
           escreva(a[i,i]:2:1, " ")
      fimpara
      escreval
      escreval
      
      escreval("MATRIZ ALTERADA: ")
      para i de 0 ate x-1 faca
           para j de 0 ate x-1 faca
                se a[i,j] < 0 entao
                   a[i,j] <- a[i,j] ^ 2
                fimse
                escreva(a[i,j]:2:1, " ")
           fimpara
           escreval
      fimpara






Fimalgoritmo