from nucleo.cris import Cris


def main():
    cris = Cris()

    print(f"Cris {cris.versao} iniciada.")
    print("Digite 'sair' para encerrar.")

    while True:
        mensagem = input("\033[32mVocê:\033[0m ")

        if mensagem.lower() == "sair":
            print("Cris: Até logo!")
            break

        resposta = cris.processar(mensagem)
        print(f"Cris: {resposta}")


if __name__ == "__main__":
    main()
