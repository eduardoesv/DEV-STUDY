glicose = float(input("Digite a medida da glicose: "))

if glicose <= 100:
    print("Classificacao: normal")
else:
    if glicose <= 140:
       print("Classificacao: elevado")
    else:
        print("Classificacao: diabetes")