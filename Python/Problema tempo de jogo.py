horaInicial = int(input("Hora inicial: "))
horaFinal = int(input("Hora final: "))
duracao = 0

if horaFinal > horaInicial:
    duracao = horaFinal - horaInicial
    print(f"O JOGO DUROU {duracao} HORA(S)")
else:
    duracao = horaFinal - horaInicial + 24
    print(f"O JOGO DUROU {duracao} HORA(S)")