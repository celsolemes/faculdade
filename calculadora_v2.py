

# Função de adição
def adicao(a, b):
    return a + b

# Função de subtração
def subtracao(a, b):
    return a - b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

# Função principal da calculadora
def calculadora(num1, num2, operacao):
    if operacao in ('+', 'soma'):
        resultado = adicao(num1, num2)
    elif operacao in ('-', 'subtracao', 'subtração'):
        resultado = subtracao(num1, num2)
    elif operacao in ('*', 'multiplicacao', 'multiplicação'):
        resultado = multiplicacao(num1, num2)
    elif operacao in ('/', 'divisao', 'divisão'):
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    
    return resultado

# Loop para interagir com o usuário
while saida.lower() != 'n': 
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Qual a operação (+, -, *, / ou digite soma, subtracao, multiplicacao, divisao): ").strip().lower()

        resultado = calculadora(num1, num2, operacao)
        print("Resultado da operação:", resultado)
    
    except ValueError:
        print("Entrada inválida! Por favor, digite números válidos.")

    saida = input("Deseja continuar? (S/N): ").strip().lower()