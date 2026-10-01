# CRIS 0.1 — Aprendizado Python

## Objetivo

A CRIS 0.1 está sendo desenvolvida como um projeto de aprendizado prático de Python.

O objetivo desta etapa é aprender Python enquanto a própria CRIS é construída.

## Método de aprendizado

O aprendizado será feito diretamente durante a construção da CRIS.

Cada novo recurso da CRIS será utilizado como uma oportunidade para aprender um conceito de Python.

A prioridade será compreender o código, testar seu funcionamento, identificar erros e corrigir problemas.

## Conteúdos de Python

Durante a construção da CRIS, serão estudados progressivamente:

- Variáveis e tipos de dados
- Entrada e saída de dados
- Condições
- Laços de repetição
- Funções
- Listas e dicionários
- Manipulação de arquivos
- Módulos e organização do código
- Tratamento de erros
- Classes e objetos
- Bibliotecas
- Banco de dados

## O que já aprendemos

### 1. Arquivos Python

Aprendemos que um programa Python pode ser armazenado em um arquivo com a extensão `.py`.

Exemplo:

    programa.py

A CRIS também é organizada em vários arquivos Python, cada um podendo ter uma responsabilidade diferente.

### 2. Execução de um programa Python

Aprendemos a executar um arquivo Python pelo terminal usando:

    python arquivo.py

Na CRIS, essa forma de execução é utilizada para testar o funcionamento do projeto.

### 3. Saída de texto

Aprendemos que o Python pode mostrar informações na tela usando `print()`.

Exemplo:

    print("Olá!")

A saída aparece diretamente no terminal.

### 4. Entrada de dados

O Python pode receber informações digitadas pelo usuário através de `input()`.

Exemplo:

    nome = input("Digite seu nome: ")

O valor recebido pode ser armazenado em uma variável.

### 5. Variáveis

Aprendemos que uma variável pode armazenar um valor para ser utilizado pelo programa.

Exemplo:

    nome = "Cristiano"

Nesse exemplo, `nome` é a variável e `"Cristiano"` é o valor armazenado.

### 6. Tipos de dados

Aprendemos que os valores utilizados pelo Python possuem tipos diferentes.

Alguns exemplos:

- `str` — texto
- `int` — número inteiro
- `float` — número decimal
- `bool` — verdadeiro ou falso

### 7. Conversão de dados

Aprendemos que dados recebidos pelo `input()` podem precisar ser convertidos.

Exemplo:

    idade = int(input("Digite sua idade: "))

Nesse caso, o texto recebido pelo `input()` é convertido para inteiro usando `int()`.

### 8. Condições

Aprendemos que programas podem tomar decisões utilizando estruturas condicionais.

Exemplo:

    if idade >= 18:
        print("Maior de idade")

A condição determina qual parte do código será executada.

### 9. Funções

Aprendemos que funções permitem organizar código que realiza uma determinada tarefa.

Exemplo:

    def saudacao():
        print("Olá!")

A função pode ser executada chamando:

    saudacao()

### 10. Arquivos e organização

Aprendemos que um projeto pode possuir vários arquivos e diretórios.

A CRIS possui uma estrutura organizada para separar suas partes.

Exemplo:

    ferramentas/
    nucleo/
    projetos/
    docs/

Essa organização permite que o projeto cresça sem concentrar tudo em um único arquivo.

### 11. Geração de programas

Uma das primeiras capacidades desenvolvidas na CRIS foi gerar programas Python.

A CRIS recebeu uma solicitação como:

    crie um programa Python para somar dois números

e passou a gerar um arquivo Python dentro do diretório `projetos`.

Isso mostrou que um programa Python pode criar e gravar outro arquivo Python.

### 12. Manipulação de arquivos

Aprendemos que o Python pode trabalhar com arquivos.

Isso permite que a CRIS futuramente possa:

- criar arquivos;
- ler arquivos;
- modificar arquivos;
- armazenar informações;
- manter registros de aprendizado.

### 13. Terminal e Shell

A construção da CRIS também está ensinando o uso do terminal.

Estamos utilizando comandos do Shell para:

- criar arquivos;
- visualizar arquivos;
- verificar diretórios;
- executar Python;
- testar o projeto;
- controlar o Git.

### 14. Documentação em Markdown

Aprendemos que o projeto pode manter sua documentação em arquivos `.md`.

O arquivo atual de aprendizado é:

    docs/aprendizado_python.md

O Markdown permite organizar a documentação usando títulos, listas e blocos de código.

### 15. Git

Aprendemos que o Git é utilizado para acompanhar as alterações do projeto.

As alterações podem ser registradas através de commits.

Isso permite manter um histórico do desenvolvimento da CRIS.

### 16. GitHub

Aprendemos que o GitHub pode armazenar uma cópia remota do projeto.

A CRIS possui um repositório no GitHub e o projeto local pode ser sincronizado com ele.

### 17. SSH

Aprendemos que o Git pode utilizar SSH para realizar a comunicação segura com o GitHub.

A autenticação SSH da CRIS foi configurada e testada com sucesso.

### 18. Testes

Aprendemos que uma alteração deve ser testada depois de implementada.

Durante a construção da CRIS, executamos o programa e observamos o resultado.

Quando aparece um erro, o erro é analisado antes de continuar.

### 19. Tratamento de erros

Aprendemos que erros fazem parte do processo de programação.

Um erro não deve ser apenas eliminado.

É importante entender:

- o que aconteceu;
- onde aconteceu;
- por que aconteceu;
- como corrigir;
- como testar novamente.

### 20. Uso do terminal para verificar arquivos

Aprendemos a utilizar comandos como:

    cat

para visualizar o conteúdo de um arquivo.

Também utilizamos:

    cat -n

para visualizar o conteúdo com números de linha.

E:

    tail -n 10

para visualizar as últimas linhas de um arquivo.

### 21. Redirecionamento

Aprendemos que o operador `>` pode ser utilizado para zerar o conteúdo de um arquivo.

Exemplo:

    > arquivo.txt

Isso é útil durante a construção da documentação quando precisamos reconstruir um arquivo do zero.

### 22. Heredoc

Aprendemos a utilizar uma estrutura como:

    cat >> arquivo <<'EOF'

    conteúdo

    EOF

Isso permite inserir várias linhas de texto em um arquivo diretamente pelo terminal.

O `EOF` é apenas um marcador utilizado para indicar onde termina o conteúdo.

## Construção da CRIS

A CRIS será construída de forma incremental.

Cada etapa deverá acrescentar uma pequena capacidade ao projeto.

Antes de avançar para uma nova etapa, o código será executado e testado.

Os erros encontrados serão analisados e corrigidos durante o processo de aprendizagem.

## Princípio do aprendizado

A CRIS não será construída apenas para funcionar.

O processo de construção também será utilizado para desenvolver o conhecimento de programação.

O código poderá ser fornecido como exemplo, mas cada parte deverá ser compreendida, testada e analisada.

Os erros fazem parte do aprendizado e serão utilizados para entender melhor como o Python funciona.

## Estado atual

A CRIS 0.1 está em fase inicial de desenvolvimento.

O foco atual é aprender Python através da construção prática do projeto.

Nesta fase, o objetivo principal não é criar uma CRIS completa, mas construir uma base sólida de programação que permita evoluir o projeto de forma gradual.

## Regra de evolução

A CRIS deverá evoluir passo a passo.

Uma nova etapa só deverá ser iniciada depois que a etapa anterior tiver sido executada, testada e compreendida.

O projeto não deve crescer apenas em quantidade de código, mas também em conhecimento sobre como cada parte funciona.

## Tratamento de erros

Os erros encontrados durante o desenvolvimento não serão tratados apenas como problemas a serem eliminados.

Cada erro deverá ser investigado para identificar sua causa e compreender o funcionamento do código.

Quando um erro for corrigido, a solução deverá ser testada novamente para confirmar que o problema foi realmente resolvido.

## Testes

Cada nova funcionalidade deverá ser testada depois de ser implementada.

Os testes deverão verificar se o comportamento do programa corresponde ao que foi planejado.

Sempre que uma alteração for feita no código, o programa deverá ser executado novamente para verificar se a alteração funcionou e se não criou novos problemas.

## Controle de versão

O desenvolvimento da CRIS será acompanhado utilizando Git.

As alterações importantes do projeto deverão ser registradas em commits.

O GitHub será utilizado como repositório remoto para manter uma cópia do projeto e acompanhar sua evolução.

O uso do Git também fará parte do aprendizado prático durante a construção da CRIS.

## Organização do código

O código da CRIS deverá ser organizado de forma clara e modular.

Cada arquivo deverá ter uma responsabilidade definida sempre que possível.

A estrutura de diretórios deverá acompanhar o crescimento do projeto, evitando concentrar toda a lógica em um único arquivo.

A organização do código também será utilizada como parte do aprendizado de Python.

## Documentação

As etapas importantes do desenvolvimento deverão ser documentadas.

A documentação deverá registrar o que foi construído, os conceitos aprendidos, os problemas encontrados e as soluções utilizadas.

O objetivo é manter um histórico compreensível da evolução da CRIS e do aprendizado durante o desenvolvimento.

## Registro de aprendizado

O aprendizado da CRIS será registrado conforme novos conceitos forem estudados e utilizados no projeto.

Cada registro deverá indicar o conceito aprendido, como ele foi utilizado, o que foi observado durante os testes e quais dificuldades ou erros foram encontrados.

O objetivo é criar um histórico prático da evolução do conhecimento em Python durante a construção da CRIS.

## Objetivo da CRIS 0.1

A CRIS 0.1 representa a primeira etapa de uma construção progressiva.

Nesta versão, o principal objetivo é desenvolver a base de programação necessária para que o projeto possa evoluir futuramente.

Cada recurso implementado deverá contribuir tanto para o funcionamento da CRIS quanto para o aprendizado necessário para desenvolver suas próximas versões.

## Evolução futura

Novos recursos poderão ser adicionados à CRIS conforme o conhecimento de programação evoluir.

Cada nova versão deverá partir da experiência adquirida nas etapas anteriores.

A evolução do projeto deverá ocorrer de forma gradual, mantendo como prioridade a compreensão do código, a estabilidade do sistema e o aprendizado.
