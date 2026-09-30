from nucleo.cris import Cris


def main():
    cris = Cris()

    print("=" * 40)
    print("           CRIS 0.1")
    print("     Assistente Python")
    print("=" * 40)
    print("Digite 'sair' para encerrar.")
    print()

    while True:
        comando = input("Você: ")

        if comando.lower() == "sair":
            print("Cris: Até logo!")
            break

        resposta = cris.processar(comando)
        print("Cris:", resposta)


if __name__ == "__main__":
    main()
