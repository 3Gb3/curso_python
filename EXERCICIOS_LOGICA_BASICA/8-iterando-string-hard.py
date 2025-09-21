frase = "O python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum."

i = 0
quantidade_que_apareceu = 0
letra_que_apareceu = ""

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    quantidade_atual = frase.count(letra_atual)

    if quantidade_que_apareceu < quantidade_atual:
        quantidade_que_apareceu = quantidade_atual
        letra_que_apareceu = letra_atual
    
    i += 1

print(f"A letra que mais apareceu foi {letra_que_apareceu} e apareceu {quantidade_que_apareceu}")