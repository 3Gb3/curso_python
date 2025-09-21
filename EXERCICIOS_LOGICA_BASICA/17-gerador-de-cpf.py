# Gerador de cpf do gb supremo

import random
import sys
import os

while True:
    quantidade_cpfs = input('Quantos cpfs gerar dessa vez? ')

    if not quantidade_cpfs.isdigit():
        os.system('cls')
        print("Digite um número inteiro")
        continue

    for indice in range(int(quantidade_cpfs)):
        novo_cpf = ''
        for cpfs in range(9):
            novo_cpf += str(random.randint(0,9))

        soma = 0
        contagem = 10
        for i in novo_cpf:
            novo_i = int(i)
            multiplicar_primeiro = novo_i * contagem
            soma += multiplicar_primeiro
            contagem -= 1
        multiplicar_tudo_primeiro = soma * 10
        restante_primeiro = multiplicar_tudo_primeiro % 11
        resultado_primeiro = 0 if restante_primeiro > 9 else restante_primeiro
        novo_cpf += str(resultado_primeiro)

        soma_2 = 0
        contagem_2 = 11
        for i in novo_cpf:
            novo_i_2 = int(i)
            multiplicar_segundo = novo_i_2 * contagem_2
            soma_2 += multiplicar_segundo
            contagem_2 -= 1
        multiplicar_tudo_segundo = soma_2 * 10
        restante_segundo = multiplicar_tudo_segundo % 11
        resultado_segundo = 0 if restante_segundo > 9 else restante_segundo
        novo_cpf += str(resultado_segundo)

        print(f"Seu {indice + 1}° cpf valido: {novo_cpf}\n")
    break