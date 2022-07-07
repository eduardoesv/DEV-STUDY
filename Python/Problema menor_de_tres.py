min = int(input("Digite a quantidade de minutos: "))
valor = 50
tarifa = 2
franquia = 100

if min < franquia:
    print(f"Valor a pagar : R$ {valor:.2f}")
else:
    adicional = (min - franquia) * tarifa
    valor = valor + adicional
    print(f"Valor a pagar : R$ {valor:.2f}")