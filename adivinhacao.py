import random

def jogar():
        print("*********************************")
        print("Bem vindo ao jogo de adivinhação!")
        print("***********************************")

        numero_secreto = round(random.randrange(1,101) )
        total_de_tentativas = 0
        acertou = False
        pontos = 1000


        print("Escolha o nivel de dificuldade: ")
        nivel = int(input("(1) Fácil (2) Médio (3) Difícil"))
        if nivel == 1:
                total_de_tentativas = 20
        elif nivel == 2:
                total_de_tentativas = 10
        else:
                total_de_tentativas = 5

        for rodada in range(0, total_de_tentativas):
                chute = int(input("Digite o seu número: "))
                if(chute < 1 or chute > 100):
                        print("Você digitou um número invalido")
                        continue
                
                acertou = chute == numero_secreto
                maior   = chute > numero_secreto
                menor   = chute < numero_secreto
                
                if(maior):
                        print("Seu chute foi maior que o número secreto")
                        pontos = pontos - abs(chute-numero_secreto)
                elif(menor):
                        print("Seu chute foi menor que o número secreto")
                        pontos = pontos - abs(chute-numero_secreto)
                elif(acertou):
                        print("Você acertou o número secreto que era {} !". format(numero_secreto) )
                        break
                        
                
        print("Você fez {}! pontos".format(pontos))  
        print("Fim de jogo!")  
        

if(__name__ == "__main__"):
       jogar() 

