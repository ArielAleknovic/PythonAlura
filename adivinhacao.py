print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto=42
chute = int(input("Digite o seu numero: "))

if numero_secreto==chute:
    print("Você acertou!")
else:
    print("Você errou!")

