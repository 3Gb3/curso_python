# Repetições
# Loop infinito = nunca acaba
# While = enquanto tal condição for verdadeira
# Break = acaba a condição
# Continue = volta para o começo do while mais proximo
# Existe o else dentro do while, que é executado após todo o codigo ser feito, mas caso tenha um break, ele não é executado

condicao = True

while condicao:  # Enquanto for verdadeiro executa infinitamente
    nome = input("Digite seu nome (sair para sair): ")
    if nome == "sair":  # Se digitar sair na variavel nome, executa fim da condição
        break

print(10 * "----")

contador = 0

while contador < 10:  # Enquanto contador menor que 10 executa
    print(contador)
    contador += 1  # Soma 1 ao contador para por fim na condição depois que chegar ao limite que nesse caso é 9

print(10 * "----")

contador = 0

while contador <= 100:
    print(contador)
    contador += 1

    if contador == 10:
        print("Victão viado")
        continue  # Contador = 10, então retorna para o while mais proximo e continua executando

print(10 * "----")

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')

print(10 * "----")