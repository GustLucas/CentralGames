# __________________________ IMPORTS ______________________
from temas import comida, profissoes, objetos, animais, paises
import random
import jogos
import time


# __________________________ MAIN _________________________
def jogar():
    # ---------------------- FUNCOES --------------------------
    def mostra(erros):
        print()
        print("TEMA: ", temas[tema][0])
        print()
        print("     ", end="")
        for letra in lista_secreta:
            print(letra, end=" ")
        print("\n")
        print("Letras usadas: ", end="")
        for letra in letras_usadas:
            print(letra, end=" ")
        print()
        print("Tentativas restantes: ", 6 - erros)
        print("_" * 80)

    # Verifica se o chute do usuário é válido
    def verifica_chute(chute):
        if chute not in lista_letras:
            print("Valor inválido. Você deve digitar uma letra de A-Z.")
            chute = input("Digite uma letra: ")
            return verifica_chute(chute)
        else:
            return chute

    # ____________________________ HEAD ____________________________________________
    print("=-=" * 11)
    print("=- Bem vindo ao jogo da forca! -=")
    print("=-=" * 11)

    temas = {
        1: ["Comidas", comida],
        2: ["Animais", animais],
        3: ["Objetos", objetos],
        4: ["Profissões", profissoes],
        5: ["Países", paises]
    }

    print(f"TEMAS: \n"
          f"(1) Comida \n"
          f"(2) Animais \n"
          f"(3) Objetos \n"
          f"(4) Profissoes \n"
          f"(5) Paises \n")

    tema = int(input("Escolha um tema: "))
    print("_" * 80)

    palavra = random.choice(temas[tema][1])

    # Criação de listas
    lista_palavra = []
    lista_secreta = []
    letras_usadas = []

    for letra in palavra:
        lista_secreta.append("_")
        lista_palavra.append(letra)

    # Separa as letras possíveis em uma lista
    letras = 'a b c ç d e f g h i j k l m n o p q r s t u v w x y z'
    lista_letras = letras.split(' ')

    qtd_erros = 0
    mostra(qtd_erros)
    ganhou = False

    # ---------------------------- GAME LOOP --------------------------------

    while qtd_erros < 6:
        acertou = False
        chute = input("Digite uma letra: ")
        chute = verifica_chute(chute)
        chute = chute.upper()

        if chute in letras_usadas:
            print(f"Você ja tentou a letra '{chute}' ")

        else:
            for letra in lista_palavra:
                if chute == letra:
                    posicao_letra = lista_palavra.index(letra)  # pega a posição da letra
                    lista_secreta[posicao_letra] = chute  # usa a posição para colocar o chute
                    lista_palavra[posicao_letra] = "-"  # remove a letra da lista original
                    acertou = True

            if not acertou:
                print("Ops! A palavra não tem a letra ", chute)
                qtd_erros += 1
            else:
                print("Boa! A palavra tem a letra ", chute)

            letras_usadas.append(chute)
            palavra_formada = ''.join(lista_secreta)  # transforma a lista em uma palavra

            if palavra_formada == palavra:
                ganhou = True
                break

        mostra(qtd_erros)

    if ganhou:
        print(f"Parabéns! Você formou a palavra '{palavra}'. ")

    else:
        print(f"Perdeu! A palavra era '{palavra}'.")

    for segundos in range(5, 0, -1):
        print(f"Voltando ao menu principal em {segundos} segundos")
        time.sleep(1)

    jogos.escolhe_jogo()


if __name__ == "__main__":
    jogar()
