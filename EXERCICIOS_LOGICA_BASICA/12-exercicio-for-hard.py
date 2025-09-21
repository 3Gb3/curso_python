# A palavra secreta é "python" (6 letras).
# Você deve mostrar a palavra oculta onde:
# Letras ainda não descobertas aparecem como (ex: p → #).
# Letras descobertas aparecem normalmente.
# Se acertar, a letra aparece na palavra oculta na posição certa.
# Se errar, apenas uma mensagem de erro aparece.
# O jogo termina quando todas as letras forem descobertas.
# Sem usar listas nem replace, só strings e índices.

morse = "python"
morse_tamanho = len(morse)
morse_oculto = morse_tamanho * "#"
quantidade_tentativas = 0

while True:
    print("\nPalavra atual:", morse_oculto)
    letra = input("Digite uma letra (ou 'sair' para desistir): ")

    if letra == "sair":
        print("Você saiu do jogo.")
        break

    # Se o jogador tenta a palavra completa
    if letra == morse:
        print("\n🎉 Parabéns, você adivinhou a palavra inteira!")
        print(f"Tentativas: {quantidade_tentativas}")
        break

    # Não permite mais de uma letra
    if len(letra) > 1:
        print("Digite apenas UMA letra ou a palavra inteira!")
        continue

    # Se a letra não existe na palavra
    if letra not in morse:
        print("❌ Letra incorreta!")
        quantidade_tentativas += 1
        continue  # vai para a próxima tentativa

    # Monta nova palavra revelando a letra acertada
    novo_morse = ""
    for i in range(morse_tamanho):
        if morse[i] == letra:
            novo_morse += letra
        else:
            novo_morse += morse_oculto[i]

    morse_oculto = novo_morse
    quantidade_tentativas += 1

    # Verifica vitória
    if morse_oculto == morse:
        print("\n✅ Parabéns, você completou a palavra:", morse)
        print(f"Tentativas: {quantidade_tentativas}")
        break