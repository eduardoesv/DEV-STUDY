x = int(input('Quantos linhas '))
y = int(input('quantas colunas '))
vet: [[int]] = [[0 for x in range(y)] for x in range(x)]

for i in range(0, x):
    for j in range(0, y):
        vet[i][j] = int(input(f'Elemento [{i},{j}]: '))

print()
print('matriz digitados:')

for i in range(0, x):
    for j in range(0, y):
        print(f'{vet[i][j]} ', end="")
    print()

print()
f = str(input('fechar? (S/N)'))