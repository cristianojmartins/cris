import os
import ast


class ProgramadorPython:

    def __init__(self):
        self.linguagem = "Python"
        self.pasta_projetos = "projetos"

        os.makedirs(self.pasta_projetos, exist_ok=True)

    def salvar_codigo(self, codigo, nome_arquivo):
        caminho = os.path.join(self.pasta_projetos, nome_arquivo)

        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(codigo)

        return caminho

    def analisar_variavel(self, comando):
        comando = comando.strip()

        if comando.lower().startswith("analise:"):
            comando = comando.split(":", 1)[1].strip()

        if "=" not in comando:
            return None

        nome, expressao = comando.split("=", 1)

        nome = nome.strip()
        expressao = expressao.strip()

        if not nome or not expressao:
            return None

        try:
            valor = ast.literal_eval(expressao)
        except Exception:
            return None

        if isinstance(valor, bool):
            tipo = "bool"
            descricao = "booleano"
        elif isinstance(valor, int):
            tipo = "int"
            descricao = "inteiro"
        elif isinstance(valor, float):
            tipo = "float"
            descricao = "float"
        elif isinstance(valor, str):
            tipo = "string"
            descricao = "string (texto)"
        else:
            tipo = type(valor).__name__
            descricao = tipo

        return {
            "nome": nome,
            "valor": valor,
            "tipo": tipo,
            "descricao": descricao
        }

    def analisar(self, comando):
        comando = comando.strip()

        if not comando:
            return "Nenhum comando recebido."

        texto = comando.lower()

        if "somar" in texto or "soma" in texto:
            codigo = '''a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

resultado = a + b

print("Resultado:", resultado)
'''

            caminho = self.salvar_codigo(codigo, "soma.py")

            return f"""Código Python criado com sucesso!

Arquivo salvo em:
{caminho}

Código:

{codigo}"""

        if "média" in texto or "media" in texto:
            codigo = '''a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

media = (a + b) / 2

print("Média:", media)
'''

            caminho = self.salvar_codigo(codigo, "media.py")

            return f"""Código Python criado com sucesso!

Arquivo salvo em:
{caminho}

Código:

{codigo}"""

        variavel = self.analisar_variavel(comando)

        if variavel:
            nome = variavel["nome"]
            tipo = variavel["tipo"]

            if tipo == "string":
                return f'{nome} é uma variável do tipo string (texto).'

            if tipo == "int":
                return f'{nome} é uma variável do tipo int (inteiro).'

            if tipo == "float":
                return f'{nome} é uma variável do tipo float.'

            if tipo == "bool":
                return f'{nome} é uma variável do tipo bool (booleano).'

            return f'{nome} é uma variável do tipo {tipo}.'

        return f"Entendi uma tarefa de programação em {self.linguagem}: {comando}"
