import subprocess
import os
from calculadora.calculadora import menu_calculadora

def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Calculadora")
        print("2. Jogo da Adivinhação (em C)")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_calculadora()
        elif escolha == "2":
            # Caminho para o executável C (compilado como 'jogo')
            caminho = os.path.join("jogo_adivinhacao", "jogo")
            # Executa o programa C
            subprocess.run([f"./{caminho}"], check=True)
        elif escolha == "0":
            print("Saindo ...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
