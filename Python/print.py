nome = str(input("Nome: "))
valor = float(input("Valor por hora: "))
horas = int(input("Horas trabalhadas: "))

pagamento = horas*valor

print(f"O pagamento para {nome} deve ser {pagamento:.2f}")