import numpy as np

print("Digite dois numeros:")
x = int(input())
y = int(input())

while x != y:
    if x > y:
        print("DECRESCENTE")
        break
    else:
        print("CRESCENTE")
        break