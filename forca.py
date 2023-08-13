def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("***********************************")

    palavra_secreta="banana"
    palavra_usuario=""
    enforcou=False
    acertou=False

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")

    



if(__name__ == "__main__"):
       jogar() 
