import os


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

        return f"Entendi uma tarefa de programação em {self.linguagem}: {comando}"
