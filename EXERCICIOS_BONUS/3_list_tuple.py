#  Exercicio realizado do site:
#  https://www.machinelearningplus.com/python/python-exercises-beginner/
#  Q3. Sequence to List and Tuple

caracteres_usuario = input('Digite os itens para lista e tupla (separados por ","): ')

def criar_lista_tupla(items):
    items = str(items)
    lista = items.split(',')
    lista = items.split()  # Remover o espaço das letras caso o usuario digite "2, 3, a, b"
    tupla = tuple(lista)
    print(lista)
    print(tupla)

criar_lista_tupla(caracteres_usuario)