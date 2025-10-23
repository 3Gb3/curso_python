#  Exercicio realizado do site:
#  https://www.machinelearningplus.com/python/python-exercises-beginner/
#  Q7. Sort Comma-Separated Words

palavras = input('Digite suas palavras para a organização (separe por ","): ')
lista_palavras = [item.strip() for item in palavras.split(',')]

def organizar_palavras(lista):
    lista_nova = sorted(lista)
    return lista_nova

print(organizar_palavras(lista_palavras))