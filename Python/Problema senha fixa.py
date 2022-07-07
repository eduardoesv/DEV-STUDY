senha = 2002
senhaDigitada = int(input("Digite a senha: "))

while senha != senhaDigitada:
    senhaDigitada = int(input("Senha Invalida! Tente novamente: "))

print("Acesso Permitido")