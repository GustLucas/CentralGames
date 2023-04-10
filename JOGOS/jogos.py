import forca
import adivinhacao

def escolhe_jogo():
    print("-" * 80)
    print(" " * 32, "MENU PRINCIPAL", " " * 32)
    print("-" * 80)

    print("\n")

    print("=-=" * 12)
    print(" " * 8, "Escolha o seu jogo!")
    print("=-=" * 12)

    print("(1) FORCA --- (2) Adivinhacao  ")

    jogo = int(input("Selecione um jogo: "))

    if jogo == 1:
        print("Jogando Forca")
        forca.jogar()

    elif jogo == 2:
        print("Jogando Advinhação")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()

