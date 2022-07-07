import math

base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

area = base * altura
perimetro = (base * 2) + (altura * 2)
diagonal = math.sqrt((base ** 2) + (altura ** 2))

print(f"AREA = {area:.2f}")
print(f"PERIMETRO = {perimetro:.2f}")
print(f"DIAGONAL = {diagonal:.2f}")