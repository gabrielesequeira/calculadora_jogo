# Calculadora Científica e Jogo de Adivinhação

Projeto da disciplina **INF1034 - Práticas de Programação**  
Feito com **Python** e **C**, combinando lógica estruturada e interatividade via terminal.

## Objetivo

Desenvolver um sistema com **duas funcionalidades principais** acessadas por um **menu interativo**:

1. **Calculadora Científica**  
   Realiza operações matemáticas básicas (adição, subtração, multiplicação, divisão) e avançadas (exponenciação e raiz quadrada).

2. **Jogo de Adivinhação**  
   Gera um número aleatório e desafia o usuário a adivinhá-lo. O programa informa se o palpite é maior ou menor até que o número correto seja encontrado.

## Funcionalidades

- [x] Menu interativo para escolher entre calculadora e jogo  
- [x] Operações matemáticas com tratamento de erros  
- [x] Geração e comparação de número aleatório  
- [x] Dicas para facilitar a adivinhação  
- [x] Integração entre programas escritos em Python e C  

## Lógica de dados do Backend

O programa principal, feito em **Python**, exibe o **menu interativo** que direciona o usuário para uma das opções:

- Ao escolher a **calculadora**, o Python executa funções que realizam os cálculos com base na entrada do usuário.
- Ao escolher o **jogo de adivinhação**, o Python chama um programa externo em **C**, que é responsável por toda a lógica do jogo, usando bibliotecas padrão para entrada/saída e geração de números aleatórios.

Essa divisão permite praticar diferentes paradigmas de programação e integrações entre linguagens.

## Estrutura de arquivos

O projeto está organizado da seguinte forma:

```bash
projeto/
│
├── calculadora.py            # Lógica da calculadora científica em Python
├── menu_principal.py         # Menu interativo principal em Python
├── jogo_adivinhacao.c        # Código do jogo de adivinhação em C
├── jogo_adivinhacao.exe      # Executável compilado do jogo (em sistemas Windows)
└── README.md                 # Documentação do projeto
```