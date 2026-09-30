class ProgramadorPython:

    def __init__(self):
        self.linguagem = "Python"

    def analisar(self, comando):
        comando = comando.strip()

        if not comando:
            return "Nenhum comando recebido."

        texto = comando.lower()

        if "somar" in texto or "soma" in texto:
            return """Código Python:

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

resultado = a + b

print("Resultado:", resultado)"""

        return f"Entendi uma tarefa de programação em {self.linguagem}: {comando}"
