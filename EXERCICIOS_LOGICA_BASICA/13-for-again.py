# Peça ao usuário uma palavra.
# Depois, construa uma nova string onde:
# As letras nas posições pares (0, 2, 4…) devem ficar em maiúsculas
# As letras nas posições ímpares (1, 3, 5…) devem ficar em minúsculas

duplicada = input("Digite uma palavra: ")
palavra_modificada = ""

for i in range(len(duplicada)):
    if i % 2 == 0:
        palavra_modificada += duplicada[i].upper()
    else:
        palavra_modificada += duplicada[i].lower()

print(palavra_modificada)

print(10 * "----")

# Peça ao usuário uma palavra.
# Depois, construa uma nova string invertida, mas com a seguinte regra:
# As letras nas posições originais pares (0, 2, 4…) devem ser substituídas por *.
# As letras nas posições originais ímpares devem aparecer normalmente, mas na ordem invertida.

texto = input("Digite sua palavra que quer invertida: ")
resultado = ""

for i in range(len(texto)-1, -1, -1):
    if i % 2 == 0:
        resultado += "*"
    else:
        resultado += texto[i]

print(resultado)

print(10 * "----")

# Peça ao usuário uma palavra.
# Depois, conte quantas vezes aparecem duas letras iguais seguidas.

duplicada = input("Digite sua palavra para ver letras duplicadas: ")
duplicada_modificada = ""
pares = 0

for i in range(len(duplicada) - 1):
    if duplicada[i] == duplicada[i + 1]:
        pares += 1
        duplicada_modificada += f'"{duplicada[i]*2}" '

print(duplicada_modificada)
print(pares)