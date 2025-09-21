# Flag (Bandeira) - Marcar um local
# None = Não valor
# is e is not = é ou não é (tipo, valor, identidade)
# id = Identidade

condicao = input("Digite 1 para True ou 0 para False: ")

try:
    condicao_bool = bool(int(condicao))  # Converte para int, depois para bool

    passou_no_if_condicao = None

    if condicao_bool is True:
        passou_no_if_condicao = True
        print("Dentro do If")
    else:
        print("Fora do If")

    if passou_no_if_condicao is not None:
        print("Passou dentro do if da condição")
    else:
        print("Não passou no if da condição")
except:
    print("Por favor, digite 0 ou 1")