from nucleo.cris import Cris

def iniciar():
    cris = Cris()

    print("Cris 0.1 iniciada.")
    print("Digite 'sair' para encerrar.")

    while True:
        mensagem = input("Você: ")

        if mensagem.strip().lower() == "sair":
            print("Cris: Até mais!")
            break

        resposta = cris.processar(mensagem)

        print("Cris:", resposta)


if __name__ == "__main__":
    iniciar()
