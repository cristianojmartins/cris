import sqlite3
from datetime import datetime


DB = "/data/data/com.termux/files/home/cris/cris.db"


def obter_hora():
    return datetime.now().strftime("%H:%M")


def buscar_no_banco(pergunta):
    db = sqlite3.connect(DB)

    resultado = db.execute(
        "SELECT resposta FROM conhecimento WHERE pergunta = ?",
        (pergunta,)
    ).fetchone()

    db.close()

    if resultado:
        return resultado[0]

    return None


def salvar_variavel(nome, valor, tipo):
    db = sqlite3.connect(DB)

    db.execute(
        "INSERT INTO variaveis (nome, valor, tipo) VALUES (?, ?, ?)",
        (nome, valor, tipo)
    )

    db.commit()
    db.close()


def analisar_linha(linha):
    partes = linha.split("=", 1)

    if len(partes) != 2:
        return "Não consegui analisar essa linha."

    variavel = partes[0].strip()
    valor = partes[1].strip()

    if valor.startswith('"') and valor.endswith('"'):
        tipo = "str"
        descricao = "string (texto)"

    elif valor.startswith("'") and valor.endswith("'"):
        tipo = "str"
        descricao = "string (texto)"

    elif valor == "True" or valor == "False":
        tipo = "bool"
        descricao = "booleano (verdadeiro ou falso)"

    elif "." in valor:
        tipo = "float"
        descricao = "float (número decimal)"

    elif valor.isdigit():
        tipo = "int"
        descricao = "inteiro"

    else:
        tipo = "desconhecido"
        descricao = "tipo desconhecido"

    salvar_variavel(variavel, valor, tipo)

    return f"{variavel} é uma variável do tipo {descricao}."


def analisar_codigo(codigo):
    linhas = codigo.splitlines()
    resultados = []

    for linha in linhas:
        if linha.strip():
            resultados.append(analisar_linha(linha))

    return "\n".join(resultados)


def consultar_variavel(texto):
    texto = texto.lower().strip()

    db = sqlite3.connect(DB)

    resultado = db.execute(
        """
        SELECT nome, tipo
        FROM variaveis
        WHERE LOWER(nome) = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (texto,)
    ).fetchone()

    db.close()

    if resultado:
        nome, tipo = resultado

        if tipo == "str":
            descricao = "string (texto)"

        elif tipo == "int":
            descricao = "inteiro"

        elif tipo == "float":
            descricao = "float (número decimal)"

        elif tipo == "bool":
            descricao = "booleano (verdadeiro ou falso)"

        else:
            descricao = "tipo desconhecido"

        return f"{nome} é uma variável do tipo {descricao}."

    return None


def responder(mensagem):
    texto = mensagem.lower().strip()

    texto = texto.replace("hotas", "horas")
    texto = texto.replace("sao", "são")

    if texto.startswith("analise:"):
        codigo = mensagem[len("analise:"):].strip()

        if codigo:
            return analisar_codigo(codigo)

        return "Envie uma linha de código depois de 'analise:'."

    if texto.startswith("qual o tipo de "):
        variavel = texto.replace(
            "qual o tipo de ",
            "",
            1
        ).strip()

        variavel = variavel.rstrip("?").strip()

        resposta = consultar_variavel(variavel)

        if resposta:
            return resposta

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

        if mensagem.lower().strip().startswith("analise:"):
            linhas = [mensagem]

            while True:
                linha = input()

                if linha.strip() == "":
                    break

                linhas.append(linha)

            mensagem = "\n".join(linhas)

        resposta = responder(mensagem)

        print()
        print("Cris:", resposta)


if __name__ == "__main__":
    iniciar()
