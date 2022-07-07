areaTerreno: float
precoTerreno: float

larguraTerreno = float(input("Digite a largura do terreno: "))
comprimentoTerreno = float(input("Digite o comprimento do terreno: "))
valorMetro2 = float(input("Digite o valor do metro quadrado: "))

areaTerreno = larguraTerreno*comprimentoTerreno
precoTerreno = areaTerreno*valorMetro2

print(f"Area do terreno = {areaTerreno:.2f}")
print(f"Preco do terreno = {precoTerreno:.2f}")