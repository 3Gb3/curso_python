#  Exercicio realizado do site:
#  https://www.machinelearningplus.com/python/python-exercises-beginner/
#  Q5. Calculate Q Values from D

# Q = ((2 * 50 * D)/30) ** 0.5


D_bruto = input('Informe os D (separados por ","): ')

def achar_valor_q(D_str):
    lista_D = [item.strip() for item in D_str.split(',')]
    D_list = []
    resultados = []

    for verificar in lista_D:
        if verificar.isdigit():
            D_list.append(int(verificar))
        else:
            print(f'Valor inválido')
            return []


    for item in D_list:
        valor_Q = ((2 * 50 * item) / 30) ** 0.5
        resultados.append(round(valor_Q))

    return resultados

resultados = achar_valor_q(D_bruto)
if resultados:
    print(resultados)