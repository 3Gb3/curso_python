# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

# Formatação básica de strings

# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - Força o número a aparecer antes dos zeros
# Sinal - + ou - / Utilizando + faz aparecer se o numero é positivo ou negativo sempre, usando - só quando for negativo
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a 
print(10 * "----")

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:0>10}')  #  10 * o 0 para a esquerda
print(f'{variavel:0<10}.')  #  10 * o 0 para a direita
print(f'{variavel:0^10}.')  #  10 * o 0 para centralizar
print(f'{1000.4873648123746:0=+10,.1f}')  # aqui estamos fazendo aparecer zeros até 10 casas, e fazendo o sinal mostrar se é positivo/negativo
print(f'O hexadecimal de 1500 é {1500:08X}')  #  8 casa de digitos até o hexadecimal
print(f'{variavel!r}')  # Não precisa saber por agora

# Fatiamento e Função len
# Fatiamento [i:f:p] [::]
# len = quantidade
print(10 * "----")

fatiamento = "Me Chamo Gabriel"
quantidade = len(fatiamento)  # Conta os espaços em branco também
print(quantidade)
print(fatiamento[3:8:1])  # Inicio / Final - 1 / Passo, de quantos em quantos pula
print(fatiamento[0::3])  # Vazio = sem limite