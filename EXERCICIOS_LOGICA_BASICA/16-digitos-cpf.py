"""
Calculo dos dígitos do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
Caso seja o primeiro digito você começara a contagem regressiva apartir do 10 e não somara o primeiro digito
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import os
import re

while True:
    cpf_usuario2 = input("Digite seu cpf, por favor: ")
    if cpf_usuario2 == "sair":
        break

    cpf_usuario = re.sub(r'[^0-9]', '', cpf_usuario2)

    try:
        cpf_int = int(cpf_usuario)
    except:
        os.system("cls")
        print("Cpf digitado incorretamente")
        print("Verifique se você digitou somente números\n")
        continue

    if (len(cpf_usuario) > 11) or (len(cpf_usuario) < 11):
            os.system("cls")
            print("Seu cpf está com tamanho incorreto\n")
            continue

    primeiro_caracter = cpf_usuario[0]
    primeiro_caracter_repetido = primeiro_caracter * 11
    if primeiro_caracter_repetido == cpf_usuario:
        print("Seu cpf está todo repetido")
        continue

    contagem = 10
    soma = 0
    for i in cpf_usuario[:9]:
        novo_i = int(i)
        multiplicacao_digitos = novo_i * contagem
        contagem -= 1
        soma += multiplicacao_digitos
    multiplicar_soma = soma * 10
    resto_divisao = multiplicar_soma % 11

    resultado_primeiro_digito = 0 if resto_divisao > 9 else resto_divisao
    print(f'O primeiro digito do cpf é: {resultado_primeiro_digito}')

    nova_contagem = 11
    nova_soma = 0
    for i in cpf_usuario[:10]:
        i_2 = int(i)
        multiplicacao_digito_2 = i_2 * nova_contagem
        nova_contagem -= 1
        nova_soma += multiplicacao_digito_2
    multiplicar_nova_soma = nova_soma * 10
    restante_nova_soma = multiplicar_nova_soma % 11

    resultado_segundo_digito = 0 if restante_nova_soma > 9 else restante_nova_soma
    print(f'O segundo digito do cpf é: {resultado_segundo_digito}')

    if (cpf_usuario[9] == str(resultado_primeiro_digito)) and (cpf_usuario[10] == str(resultado_segundo_digito)):
        print("Seu cpf é valido")
        continue
    else:
        print("Digite um cpf valido, por favor")
        continue