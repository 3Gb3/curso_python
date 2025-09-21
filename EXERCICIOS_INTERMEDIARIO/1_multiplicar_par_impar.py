# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar():
    total = 1
    while True:
        numero_usuario = input("Digite o número (sair): ")
        if numero_usuario == "sair":
            break
        try:
            numero_int = int(numero_usuario)
        except ValueError:
            print("Digite apenas números")
        total *= numero_int
        print(f"Resultado = {total}")
    print(f"Total Final = {total}")
    return total

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def pares():
    while True:
        numero_usuario = input("Digite o número (sair): ")
        if numero_usuario == "sair":
            break
        try:
            numero_int = int(numero_usuario)
        except ValueError:
            print("Digite apenas números")
        if (numero_int % 2) == 0:
            print("É par")
        else:
            print("É impar")

resposta = input("Deseja acessar o (multiplicar) ou verificar (pares)? ").lower().strip()
if resposta == "multiplicar":
    multiplicar()
elif resposta == "pares":
    pares()
else:
    print("Digite uma das opções")