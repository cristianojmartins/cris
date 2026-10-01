import sqlite3
from datetime import datetime


def obter_hora():
    return datetime.now().strftime("%H:%M")


def buscar_no_banco(pergunta):
    db = sqlite3.connect("cris.db")

    resultado = db.execute(
        "SELECT resposta FROM conhecimento WHERE pergunta = ?",
        (pergunta,)
    ).fetchone()

    db.close()

    if resultado:
        return resultado[0]

    return None


def analisar_linha(linha):
    partes = linha.split("=")

    if len(partes) != 2:
        return "Não consegui analisar essa linha."

    variavel = partes[0].strip()
    valor = partes[1].strip()

    if valor.startswith('"') and valor.endswith('"'):
        tipo = "str"

    elif valor.startswith("'") and valor.endswith("'"):
        tipo = "str"

    elif valor == "True" or valor == "False":
        tipo = "bool"

    elif "." in valor:
        tipo = "float"

    elif valor.isdigit():
        tipo = "int"

    else:
        tipo = "desconhecido"

    return f"{variavel} → variável → {tipo}"


def analisar_codigo(codigo):
    linhas = codigo.splitlines()
    resultados = []

    for linha in linhas:
        if linha.strip():
            resultados.append(analisar_linha(linha))

    return "\n".join(resultados)


def responder(mensagem):
    texto = mensagem.lower().strip()

    texto = texto.replace("hotas", "horas")
    texto = texto.replace("sao", "são")

    if texto.startswith("analise:"):
        codigo = mensagem[len("analise:"):].strip()

        if codigo:
            return analisar_codigo(codigo)

        return "Envie uma linha de código depois de 'analise:'."

    resposta = buscar_no_banco(texto)

    if resposta:
        return resposta

    if "hora" in texto or "horas" in texto:
        return f"Agora são {obter_hora()}."

    return "Ainda não sei responder isso, mas podemos me ensinar."


def iniciar():
    print("Cris 0.1 iniciada.")
    print("Digite 'sair' para encerrar.")

    while True:
        mensagem = input("Você: ")

        if mensagem.lower().strip() == "sair":
            print("Cris: Até mais!")
            break

        resposta = responder(mensagem)
        print("Cris:", resposta)


iniciar()
