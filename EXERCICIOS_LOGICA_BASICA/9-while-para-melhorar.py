# Crie um programa que:
# Peça para o usuário digitar números inteiros infinitamente.
# Se o usuário digitar 0, o programa deve parar.
# Enquanto isso, ele deve somar todos os números positivos e contar quantos números negativos foram digitados.
# No final, mostre:
# a soma dos positivos
# e quantos negativos foram digitados

negativos = 0
soma_dos_positivos = 0

while True:
    numero = input("Digite um número (0 para cancelar): ")
    try:
        numero_float = float(numero)
    except:
        print("Digite um número por favor: ")
    if numero_float == 0:
        break
    elif numero_float >0:
        soma_dos_positivos += numero_float
    else:
        negativos += 1

print(f"Soma dos positivos é {soma_dos_positivos} e a quantidade de negativos é {negativos}")