# Scientific Calculator and Guessing Game

Project for the course **INF1034 - Programming Practices**  
Built with **Python** and **C**, combining structured logic and terminal interactivity.

## Objective

Develop a system with **two main functionalities** accessed through an **interactive menu**:

1. **Scientific Calculator**  
   Performs basic mathematical operations (addition, subtraction, multiplication, division) and advanced operations (exponentiation and square root).

2. **Guessing Game**  
   Generates a random number and challenges the user to guess it. The program informs if the guess is higher or lower until the correct number is found.

## Features

- [x] Interactive menu to choose between calculator and game  
- [x] Mathematical operations with error handling  
- [x] Random number generation and comparison  
- [x] Hints to ease guessing  
- [x] Integration between programs written in Python and C  

## Backend Data Logic

The main program, made in **Python**, displays the **interactive menu** that directs the user to one of the options:

- When choosing the **calculator**, Python executes functions that perform calculations based on user input.
- When choosing the **guessing game**, Python calls an external program written in **C**, which is responsible for all the game logic, using standard libraries for input/output and random number generation.

This division allows practicing different programming paradigms and language integrations.

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
