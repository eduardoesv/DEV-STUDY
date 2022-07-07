print("Digite as idades:")
x = int(input())
y = 0
z = 0

if x < 0:
    print("IMPOSSIVEL CALCULAR")
else:    
    while x > 0:
        z = z+1
        y = x + y
        x = int(input())
    media = y / z
    print(f"MEDIA = {media:.2f}")