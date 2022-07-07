posicao = int(input("Posição desejada:"))
fibonacci = 1
valor1 = 0
valor2 = 1

print(fibonacci)
for i in range(0,posicao):
    fibonacci = valor1 + valor2
    valor1 = valor2
    valor2 = fibonacci
    print(fibonacci)