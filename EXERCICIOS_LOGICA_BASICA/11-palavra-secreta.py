# Faça um jogo para o usuário adivinhar qual a palavra secreta.
# - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
# - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
# - Se a letra digitada estiver na palavra secreta; exiba a letra;
# - Se a letra digitada não estiver na palavra secreta; exiba *. Faça a contagem de tentativas do seu usuário.

import os

palavra_secreta = "bolsonaro"
quantidade_letras = len(palavra_secreta)
palavra_oculta = "*" * quantidade_letras
quantidade_tentativas = 0

while True:
    letra = input("Adivinhe a letra (sair para sair): ")
    if letra == "sair":
        print("Obrigado por jogar")
        break
    elif len(letra) > 1:
        print("Digite apenas uma letra")
        continue

    nova_oculta = ""  # zera antes de montar a nova versão

    for i in range(quantidade_letras):
        if palavra_secreta[i] == letra:
            nova_oculta += letra
        else:
            nova_oculta += palavra_oculta[i]

    palavra_oculta = nova_oculta
    print(palavra_oculta)
    quantidade_tentativas += 1
    if palavra_oculta == palavra_secreta:
        os.system("cls")
        print("Parabéns, você ganhou")
        print(f"Suas tentativas foram {quantidade_tentativas}")
        continue