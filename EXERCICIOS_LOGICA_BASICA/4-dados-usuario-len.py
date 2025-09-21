# Poderia simplicar colocando muitas coisas dentro da F-String, mas preferi criar variaveis para caso queira chamar esse valor mais para frente eu consiga utiliza-lo
nome = input("Qual seu nome: ")
idade = input("Qual sua idade: ")

if nome and idade:
    quantidade_letras = len(nome)
    tem_espaco = False
    nome_invertido = nome[::-1]
    primeira_letra = nome[0]
    ultima_letra = nome[-1]
    
    if " " in nome:
        tem_espaco = True
    
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")
    print(f"Espaços no nome: {tem_espaco}")
    print(f"Seu nome tem {quantidade_letras} letras")
    print(f"A primeira letra do seu nome é {primeira_letra}")
    print(f"A ultima letra do seu nome é {ultima_letra}")
else:
    print("Algum dado não foi digitado")