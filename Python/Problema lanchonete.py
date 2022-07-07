codigoDeProduto = int(input("Codigo do produto comprado: "))
qtdComprada = int(input("Quantidade comprada:"))

def valordoproduto(codigoDeProduto):
    match codigoDeProduto:
        case 1:
            return 5.00
        case 2:
            return 3.50
        case 3:
            return 4.80
        case 4:
            return 8.90
        case 5:
            return 7.32
        case _:
            return "Codigo invalido"

valor = valordoproduto(codigoDeProduto)

if valor != "Codigo invalido":
    valortotal = valor * qtdComprada
    print(f"Valor a pagar: R$ {valortotal:.2f}")       
else:
    print("Codigo invalido") 