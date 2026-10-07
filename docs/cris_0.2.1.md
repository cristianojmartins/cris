# CRIS 0.2.1 — Diferenças em relação à CRIS 0.2.0

## Objetivo

A CRIS 0.2.1 é uma versão de consolidação da CRIS 0.2.0.

O foco desta versão foi organizar, corrigir e validar o estado atual do projeto.

## Principais diferenças

### 1. Testes completos

A CRIS 0.2.1 passou por uma bateria de 21 testes automatizados.

Resultado:

- 21 testes executados
- 21 testes aprovados
- 0 testes com erro
- 100% de aprovação

### 2. Validação das variáveis

Foram validados os principais tipos de variáveis:

- `string`
- `int`
- `float`
- `bool`

Também foi validada a consulta do tipo de cada variável.

### 3. Persistência SQLite

Foi validado o funcionamento do banco `cris.db`, incluindo:

- tabela `conhecimento`
- tabela `variaveis`
- armazenamento das variáveis
- recuperação das variáveis armazenadas

### 4. Projetos existentes

Foi confirmada a existência dos projetos:

- `projetos/soma.py`
- `projetos/media.py`

### 5. Código e documentação

A versão 0.2.1 consolida alterações realizadas em:

- `main.py`
- `nucleo/cris.py`
- `docs/cris_0.2.0.md`
- `ferramentas/professor_python.py`
- `testar_cris.py`

## Git

Versão:

`v0.2.1`

Commit:

`ad3fe6a`

Mensagem:

`CRIS 0.2.1 - todos os testes passando`

## Estado da versão

**CRIS 0.2.1 — versão de referência**

**21/21 testes aprovados — 100% OK.**
