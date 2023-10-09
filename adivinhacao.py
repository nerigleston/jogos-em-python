import random


def jogar():

    print("********************************")
    print("Bem vindo ao jogo de Advinhação!")
    print("********************************")

    numeroSecreto = random.randrange(1, 101)
    totalDeTentativas = 0
    pontos = 100

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        totalDeTentativas = 20
    elif (nivel == 2):
        totalDeTentativas = 10
    else:
        totalDeTentativas = 5
    print(f"Você tem o total de {totalDeTentativas} tentativas")

    for rodada in range(1, totalDeTentativas + 1):

        print(f"Tentativa: {rodada} de {totalDeTentativas}")
        chute = int(input("Digite o seu número entre 1 e 100: "))
        print(f"Você digitou {chute}")

        if (chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100!")
            continue

        acertou = chute == numeroSecreto
        maior = chute > numeroSecreto
        menor = chute < numeroSecreto

        if (acertou):
            print("Você acertou o número secreto!")
            print(f"Número acertado na {rodada}ª rodada e fez {pontos}")
            break
        else:
            if (maior):
                print("Você errou! Chute maior que o número secreto!")
            elif (menor):
                print("Você errou! Chute menor que o número secreto!")

            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos
        print("********************************")

    print(f"O número secreto foi {numeroSecreto}")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
