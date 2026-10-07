from nucleo.cris import Cris
from ferramentas.programador import ProgramadorPython


def teste(nome, resultado):
    if resultado:
        print(f"[OK] {nome}")
        return 1
    else:
        print(f"[ERRO] {nome}")
        return 0


print("=" * 30)
print(" TESTE DA CRIS 0.1")
print("=" * 30)

total = 0
sucessos = 0

# -------------------------
# 1. Núcleo da CRIS
# -------------------------

cris = Cris()

total += 1
sucessos += teste(
    "Núcleo",
    cris.nome == "Cris"
)

# -------------------------
# 2. Saudação
# -------------------------

total += 1
sucessos += teste(
    "Saudação",
    "Olá" in cris.processar("oi")
)

# -------------------------
# 3. Programador Python
# -------------------------

programador = ProgramadorPython()

# String
total += 1
sucessos += teste(
    "Identificação de string",
    "string" in programador.analisar(
        'nome = "Cristiano"'
    ).lower()
)

# Float
total += 1
sucessos += teste(
    "Identificação de float",
    "float" in programador.analisar(
        "altura = 1.75"
    ).lower()
)

# Integer
total += 1
sucessos += teste(
    "Identificação de inteiro",
    "inteiro" in programador.analisar(
        "idade = 49"
    ).lower()
)

# -------------------------
# 4. Geração de programa
# -------------------------

total += 1
sucessos += teste(
    "Gerador de soma",
    "float" in programador.analisar(
        "crie um programa Python para somar dois números"
    )
)

# -------------------------
# Resultado
# -------------------------

print()
print("=" * 30)
print(f" RESULTADO: {sucessos}/{total}")
print("=" * 30)

if sucessos == total:
    print("CRIS 0.1: todos os testes passaram!")
else:
    print("CRIS 0.1: existem testes com erro.")
