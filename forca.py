import random


def jogar():

    print("********************************")
    print("***Bem vindo ao jogo de Forca!**")
    print("********************************")

    palavras = ["casa", "carro", "cachorro"]
    palavra_secreta = palavras[random.randint(0, len(palavras) - 1)]

    acertos = []
    erros = 0

    for i in range(6):
        for letra in palavra_secreta:
            if letra in acertos:
                print(letra)
            else:
                print("_")

        chute = input("Chute uma letra: ")

        if chute in palavra_secreta:
            acertos.append(chute)
        else:
            erros += 1

        if palavra_secreta == "".join(acertos):
            break

    if erros == 6:
        print("Você perdeu!")
    else:
        print("Você ganhou!")

    print("********************************")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
