import math

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

delta = b**2 - (4*a*c)

if (a<b) and (a<c):
    print(f"MENOR = {a}")
elif b<c:
    print(f"MENOR = {b}")
else:
    print(f"MENOR = {c}")

    