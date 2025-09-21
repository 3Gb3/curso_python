#  Todas as atividades podem ser feitas utilizando o isdigit(), apenas preferi usar o try
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_digitado = input("Digite um número inteiro para verificar se é par ou ímpar: ")
try:
    numero_int = int(numero_digitado)
    restante = numero_int % 2
    if restante == 0:
        print("O número digitado é par")
    else:
        print("O número digitado é ímpar")
except:
    print("Não é um número inteiro")
print(10 * "-----")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_usuario = input("Digite a hora do dia por favor, apenas números inteiros: ")
try:
    hora_int = int(hora_usuario)
    bom_dia = 0 <= hora_int <= 11
    boa_tarde = 12 <= hora_int <= 17
    boa_noite = 18 <= hora_int <= 23
    if bom_dia:
        print("Bom dia")
    elif boa_tarde:
        print("Boa tarde")
    else:
        print("Boa Noite")
except:
    print("Informe a hora em número inteiro por favor 0-23")
print(10 * "-----")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome: ")
quantidade_letras_nome = len(nome)
nome_curto = quantidade_letras_nome <= 4
nome_normal = 5 <= quantidade_letras_nome <= 6
nome_grande = quantidade_letras_nome > 6

if nome_curto:
    print("Você tem um nome curto")
elif nome_normal:
    print("Você tem um nome normal")
else:
    print("Você tem um nome grande")