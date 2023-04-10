# __________________________ IMPORTS ________________________________
import jogos
from random import randint
import time


# __________________________ MAIN ___________________________________
def jogar():
    # __________________________ FUNCOES ________________________________

    def condicoes():
        chute = int(input("Digite um número de 1 até 100: \n"))
        if chute < 1 or chute > 100:
            print("Número invalido. O número deve estar entre 1 e 100!")

        elif chute > numero_secreto:
            print(f"Errou! O número secreto é menor que {chute}.")
            print("=-=" * 10)

        elif chute < numero_secreto:
            print(f"Errou! O número secreto é maior que {chute}.")
            print("=-=" * 10)

        else:
            if chute == numero_secreto:
                print(f"Parabéns, o número secreto era {chute}")
                print(f"Você acertou em {tentativa} tentativas")
                return True

    # __________________________ JOGO ____________________________________

    print("=-=" * 12)
    print("Bem vindo ao jogo de adivinhação!")
    print("=-=" * 12)
    print("Dificuldades:\n",
          "(1) Facil\n",
          "(2) Médio\n",
          "(3) Difícil\n",
          )

    while True:
        dificuldade = int(input("Escolha a dificuldade do jogo: "))

        if dificuldade == 1 or dificuldade == 2 or dificuldade == 3:
            break
        else:
            print("Número inválido.")

    numero_secreto = randint(1, 100)
    acertou = False
    tentativa = 1

    if dificuldade == 1:
        print("Na dificuldade fácil você tem direito a quantas tentativas precisar!")
        while not acertou:
            acertou = condicoes()
            tentativa += 1

    if dificuldade == 2:
        print("Na dificuldade média você tem direito a apenas 7 tentativas!")
        for tentativa in range(1, 7+1):
            if acertou:
                break

            acertou = condicoes()

        if not acertou:
            print(f"Perdeu! O número secreto era {numero_secreto}")

    if dificuldade == 3:
        print("na dificuldade díficil você tem direito a apenas 5 tentativas!")
        for tentativa in range(1, 5+1):
            if acertou:
                break

            acertou = condicoes()

        if not acertou:
            print(f"Perdeu! O número secreto era {numero_secreto}")

    for segundos in range(5, 0, -1):
        print(f"Voltando ao menu principal em {segundos} segundos")
        time.sleep(1)

    jogos.escolhe_jogo()


if __name__ == "__main__":
    jogar()
