import sqlite3
from ferramentas.programador import ProgramadorPython


class Cris:

    def __init__(self):
        self.nome = "Cris"
        self.versao = "0.1"
        self.estado = "inicial"
        self.programador = ProgramadorPython()
        self.banco = "cris.db"

    def consultar_conhecimento(self, pergunta):
        pergunta = pergunta.strip().lower()
        pergunta = pergunta.rstrip("?!.")

        conexao = sqlite3.connect(self.banco)
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT resposta FROM conhecimento WHERE pergunta = ?",
            (pergunta,)
        )

        resultado = cursor.fetchone()

        conexao.close()

        if resultado:
            return resultado[0]

        return None

    def processar(self, comando):

        comando = comando.strip()

        if not comando:
            return "Estou aguardando um comando."

        texto = comando.lower()

        if texto in ["oi", "olá", "ola"]:
            return "Olá! Eu sou a Cris."

        if "seu nome" in texto:
            return f"Meu nome é {self.nome}."

        if "versão" in texto or "versao" in texto:
            return f"Estou na versão {self.versao}."

        if "estado" in texto:
            return f"Meu estado atual é: {self.estado}."

        conhecimento = self.consultar_conhecimento(texto)

        if conhecimento:
            return conhecimento

        if "python" in texto:
            return self.programador.analisar(comando)

        return f"Recebi: {comando}"


if __name__ == "__main__":
    pass
