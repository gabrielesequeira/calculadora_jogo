import math

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def exponenciar(a, b):
    return math.pow(a, b)

def raiz_quadrada(a):
    if a < 0:
        return "Erro: raiz de número negativo"
    return math.sqrt(a)

def menu_calculadora():
    while True:
        print("\n=== Calculadora Científica ===")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Exponenciação")
        print("6. Raiz quadrada")
        print("0. Voltar")

        escolha = input("Escolha a operação: ")

        if escolha == "0":
            break

        try:
            if escolha in ["1", "2", "3", "4", "5"]:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            elif escolha == "6":
                a = float(input("Digite o número: "))
        except ValueError:
            print("Entrada inválida. Use apenas números.")
            continue

        if escolha == "1":
            print("Resultado:", somar(a, b))
        elif escolha == "2":
            print("Resultado:", subtrair(a, b))
        elif escolha == "3":
            print("Resultado:", multiplicar(a, b))
        elif escolha == "4":
            print("Resultado:", dividir(a, b))
        elif escolha == "5":
            print("Resultado:", exponenciar(a, b))
        elif escolha == "6":
            print("Resultado:", raiz_quadrada(a))
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_calculadora()
