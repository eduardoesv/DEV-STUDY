escala = str(input("Voce vai digitar a temperatura em qual escala (C/F)? "))
F = 0
C = 0

if escala == "F":
    F = float(input("Digite a temperatura em Fahrenheit: "))
    C = (F-32) / 1.8
    print(f"Temperatura equivalente em Celsius: {C:.2f}")
elif escala == "C":    
    C = float(input("Digite a temperatura em Celsius: "))
    F = C * 1.8 + 32
    print(f"Temperatura equivalente em Fahrenheit: {F:.2f}")    