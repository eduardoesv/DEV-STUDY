print("Digite dois numeros inteiros: ")
n1 = int(input())
n2 = int(input())

if n1 % n2 == 0:
    print("Sao Multiplos")
elif n2 % n1 == 0:
    print("Sao Multiplos")
else:
    print("Nao sao multiplos")
