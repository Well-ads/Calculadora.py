"""
Módulo calculadora.

Este módulo oferece funções para 
realizar operações matemáticas básicas.
"""

def somar_num(x, y):
    """
    Soma dois números e retorna o resultado.
    """
    soma = x + y
    return soma

def subtrair_num(x, y):
    """
    Subtrai o segundo número do primeiro e retorna o resultado.
    """
    subtracao = x - y
    return subtracao

def multiplicar_num(x, y):
    """
    Multiplica dois números e retorna o resultado.
    """
    mult = x * y
    return mult

def dividir_num(x, y):
    """
    Divide o primeiro número pelo segundo, 
    tratando o caso de divisão por zero.
    """
    if y == 0:
        print("Erro: Divisão por zero.")
        return None
    div = x / y
    return div

def calcula_num():
    """
    Função principal da calculadora que solicita entradas do usuário.
    """
    print("Calculadora")

    try:
        x = int(
            input("Digite o primeiro número: ")
        )
        y = int(
            input("Digite o segundo número: ")
        )
    except ValueError:
        print("Erro: Você deve digitar números inteiros.")
        return

    operacao = input(
        "Escolha a operação (+, -, *, /): "
    )

    if operacao == "+":
        resultado = somar_num(x, y)
    elif operacao == "-":
        resultado = subtrair_num(x, y)
    elif operacao == "*":
        resultado = multiplicar_num(x, y)
    elif operacao == "/":
        resultado = dividir_num(x, y)
    else:
        print("Operação inválida")
        return

    if resultado is not None:
        print("Resultado:", resultado)

if __name__ == "__main__":
    calcula_num()
