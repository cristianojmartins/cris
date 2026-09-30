from ferramentas.programador import ProgramadorPython


class Cris:

    def __init__(self):
        self.nome = "Cris"
        self.versao = "0.1"
        self.estado = "inicial"
        self.programador = ProgramadorPython()

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

        if "python" in texto:
            return self.programador.analisar(comando)

        return f"Recebi: {comando}"
