primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

# Não era pra converter para número KAKAKAKA

primeiro_valor_n = (primeiro_valor)
segundo_valor_n = (segundo_valor)

if primeiro_valor_n > segundo_valor_n:
    print(f"{primeiro_valor_n=} é maior que {segundo_valor_n=}.")
elif primeiro_valor_n < segundo_valor_n:
    print(f"{primeiro_valor_n=} é menor que {segundo_valor_n=}.")
elif primeiro_valor_n == segundo_valor_n:
    print(f"{primeiro_valor_n=} é igual a {segundo_valor_n=}.")
else:
    print("Valores inválidos para comparação.")