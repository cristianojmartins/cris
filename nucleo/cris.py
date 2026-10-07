import sqlite3
import re
from ferramentas.programador import ProgramadorPython


class Cris:

    def __init__(self):
        self.nome = "Cris"
        self.versao = "0.1"
        self.estado = "inicial"
        self.programador = ProgramadorPython()
        self.banco = "cris.db"

        self.preparar_banco()

    def preparar_banco(self):
        conexao = sqlite3.connect(self.banco)
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conhecimento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pergunta TEXT NOT NULL,
                resposta TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS variaveis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                valor TEXT NOT NULL,
                tipo TEXT NOT NULL
            )
        """)

        cursor.execute("""
            UPDATE variaveis
            SET tipo = 'string'
            WHERE tipo = 'str'
        """)

        conexao.commit()
        conexao.close()

    def consultar_conhecimento(self, pergunta):
        pergunta = pergunta.strip().lower()
        pergunta = pergunta.rstrip("?!. ")

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

    def salvar_variavel(self, nome, valor, tipo):
        conexao = sqlite3.connect(self.banco)
        cursor = conexao.cursor()

        if isinstance(valor, bool):
            valor_salvo = str(valor)
        else:
            valor_salvo = str(valor)

        cursor.execute(
            "SELECT id FROM variaveis WHERE nome = ? ORDER BY id",
            (nome,)
        )

        registros = cursor.fetchall()

        if registros:
            primeiro_id = registros[0][0]

            cursor.execute(
                """
                UPDATE variaveis
                SET valor = ?, tipo = ?
                WHERE id = ?
                """,
                (valor_salvo, tipo, primeiro_id)
            )

            ids_extras = [registro[0] for registro in registros[1:]]

            for id_extra in ids_extras:
                cursor.execute(
                    "DELETE FROM variaveis WHERE id = ?",
                    (id_extra,)
                )

        else:
            cursor.execute(
                """
                INSERT INTO variaveis (nome, valor, tipo)
                VALUES (?, ?, ?)
                """,
                (nome, valor_salvo, tipo)
            )

        conexao.commit()
        conexao.close()

    def consultar_variavel(self, nome):
        nome = nome.strip()

        conexao = sqlite3.connect(self.banco)
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT valor, tipo
            FROM variaveis
            WHERE nome = ?
            ORDER BY id DESC
            LIMIT 1
            """,
            (nome,)
        )

        resultado = cursor.fetchone()

        conexao.close()

        return resultado

    def analisar_variavel(self, comando):
        variavel = self.programador.analisar_variavel(comando)

        if not variavel:
            return None

        nome = variavel["nome"]
        valor = variavel["valor"]
        tipo = variavel["tipo"]

        self.salvar_variavel(nome, valor, tipo)

        if tipo == "string":
            return f'{nome} é uma variável do tipo string (texto).'

        if tipo == "int":
            return f'{nome} é uma variável do tipo int (inteiro).'

        if tipo == "float":
            return f'{nome} é uma variável do tipo float.'

        if tipo == "bool":
            return f'{nome} é uma variável do tipo bool (booleano).'

        return f'{nome} é uma variável do tipo {tipo}.'

    def consultar_tipo_variavel(self, comando):
        padrao = r"qual\s+o\s+tipo\s+de\s+([a-zA-Z_]\w*)\s*\??"

        resultado = re.search(padrao, comando.strip().lower())

        if not resultado:
            return None

        nome = resultado.group(1)

        dados = self.consultar_variavel(nome)

        if not dados:
            return f"Não encontrei a variável '{nome}'."

        valor, tipo = dados

        if tipo == "string":
            descricao = "string (texto)"
        elif tipo == "int":
            descricao = "int (inteiro)"
        elif tipo == "float":
            descricao = "float"
        elif tipo == "bool":
            descricao = "bool (booleano)"
        else:
            descricao = tipo

        return f"A variável {nome} é do tipo {descricao}."

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

        if texto.startswith("analise:"):
            resposta = self.analisar_variavel(comando)

            if resposta:
                return resposta

        resposta_tipo = self.consultar_tipo_variavel(comando)

        if resposta_tipo:
            return resposta_tipo

        conhecimento = self.consultar_conhecimento(texto)

        if conhecimento:
            return conhecimento

        if "python" in texto:
            return self.programador.analisar(comando)

        return f"Recebi: {comando}"


if __name__ == "__main__":
    pass
