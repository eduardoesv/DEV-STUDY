Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 07/02/2022
Var
        a, b, c, x1, x2, delta : real

Inicio
        escreva("Coeficiente a: ")
        leia(a)
        escreva("Coeficiente b: ")
        leia(b)
        escreva("Coeficiente c: ")
        leia(c)
        
        delta <- (b^2)-(4*a*c)
        x1 <- ((b*-1)+RaizQ(abs(delta)))/(2*a)
        x2 <- ((b*-1)-RaizQ(abs(delta)))/(2*a)
        
        se (delta<0) ou (a=0) entao
           escreva("Esta equacao nao possui raizes reais")
        senao
           escreval("X1 = ", x1:1:4)
           escreval("X2 = ", x2:1:4)
        fimse
Fimalgoritmo