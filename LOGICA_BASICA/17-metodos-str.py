# split e join com list e str
# split -> divide uma string em uma lista
# join  -> junta elementos de uma lista em uma string

frase = "            Testando as funções,          está bem legal"

# Usando split(',') para dividir a string original em uma lista, separando pelo caractere ','
# Assim teremos duas partes: antes da vírgula e depois da vírgula
nova_frase_crua = frase.split(',')
# Exemplo: ["            Testando as funções", "          está bem legal"]

# O código comentado abaixo faria o mesmo que o for mais abaixo,
# percorrendo a lista e removendo espaços extras com strip()
# for i, palavra in enumerate(nova_frase_crua):
#     nova_frase_crua[i] = nova_frase_crua[i].strip()

print(nova_frase_crua)  # Mostra a lista original com os espaços em excesso

print(10 * "----")  # Imprime uma linha de separação visual

# Esse método é melhor porque cria uma nova lista sem modificar a original
nova_frase_fixed = []

# Percorre a lista criada pelo split()
for i, teste in enumerate(nova_frase_crua):
    # Remove espaços antes e depois de cada elemento e adiciona na nova lista
    nova_frase_fixed.append(nova_frase_crua[i].strip())

print(nova_frase_fixed)  # Mostra a lista já sem os espaços extras

# Agora vamos unir os elementos da lista em uma única string
# join(", ") une os elementos com vírgula e espaço entre eles
frases_unidas = ", ".join(nova_frase_fixed)
print(frases_unidas)  # Exibe a string final "Testando as funções, está bem legal"