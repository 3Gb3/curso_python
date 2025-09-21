print("- Calculadora Do Gb - ")

while True:

    # input do usúario

    num1 = input("Digite seu primeiro número (sair para sair): ")
    if num1.lower() == "sair":
        break
    num2 = input("Digite seu segundo número (sair para sair): ")
    if num2.lower() == "sair":
        break
    operador = input ("Digite um operador apenas->(+-/*) (sair para sair) : ")
    if operador.lower() == "sair":
        break
    resultado = 0

    # teste dos números e operadores

    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except:
        print("Digite um número valido")
        continue

    operadores_validos = "+-*/"
    if len(operador) > 1:
        print("Digite apenas um operador")
        continue
    if operador not in operadores_validos:
        print("Por favor, digite um operador valido")
        continue

    # Resolvendo as contas

    if operador == "-":
        resultado = num1_float - num2_float

    if operador == "+":
        resultado = num1_float + num2_float

    if operador == "*":
        resultado = num1_float * num2_float

    if operador == "/":
        if num2_float == 0:
            print("Divisão por zero é impossivel")
            continue
        else:
            resultado = num1_float / num2_float

    # Resultados

    print(f"O resultado de {num1_float} {operador} {num2_float} é {resultado:.2f}")

    # Sair ou Continuar

    sair = input("Você deseja sair da calculadora? Sim ou Não: ").lower()
    if sair == "sim":
        break
    else:
        print(10 * "----")
        continue

print("Obrigado por usar a calculadora do Gb")