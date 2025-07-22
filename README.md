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
## Topics Learned and Practiced

During the development of this project, several concepts were addressed and applied:

- **Program structure with interactive menu**
  - Implementation of simple terminal interfaces for feature selection

- **Mathematical operations in Python**
  - Basic calculations (addition, subtraction, multiplication, division)
  - Advanced operations (exponentiation, square root)
  - Exception handling to prevent input errors, such as division by zero

- **Cross-language integration**
  - Communication between Python and external programs written in C
  - Execution of C programs from Python scripts

- **Input and output handling**
  - Receiving user input via terminal
  - Displaying messages and interactive feedback

- **Basic concepts of structured programming in C**
  - Standard input and output (`stdio.h`)
  - Use of libraries for random number generation (`stdlib.h`, `time.h`)
  - Loops and conditional statements for game control


