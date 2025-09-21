# Na atividade 6 vimos como iterar uma string com while, mas com for isso se torna muito mais facil
# O for é basicamente um laço de repetição que nos sabemos previamente qual vai ser o valor dele
# For + Range
# range -> range(start, stop, step) // caso não seja definido, o unico numero é o STOP do range
# Iterando string com for:
texto = "Python"
novo_texto = ""

for i in texto:  # o for percorre cada indice da string automaticamente, então aqui o i assume o valor desse indice
    novo_texto += f"*{i}"
print(f"{novo_texto}*")

print(10 * "----")

# Como o for funciona:
# Iterável -> str, range, etc (__iter__)
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue seu iterador

nome = "Luiz"
iterator = iter(nome)
novo_nome = ""
while True:  # Basicamente fizemos o exercicio de cima, mas utilizando while, mas utilizamos os fundamentos que o for utiliza
    try:
        letra = next(iterator)
        novo_nome += f"*{letra}"
    except StopIteration:
        novo_nome += "*"
        print(novo_nome)
        break

print(10 * "----")

# Podemos também utilizar os conhecimentos de while dentro de um for
# continue/break/else,etc

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')