precoProduto = float(input("Preço unitário do produto: "))
qtdCompra = int(input("Quantidade comprada: "))
vlrRecebido = float(input("Dinheiro recebido: "))

troco = vlrRecebido-(precoProduto*qtdCompra)

print(f"TROCO = {troco:.2f}")