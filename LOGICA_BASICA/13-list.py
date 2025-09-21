# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis:
#     append, insert, pop, del, clear, extend, +
# Create Read Update   Delete
# Criar, ler, alterar, apagar = lista[i] (CRUD)
# Quando atribuimos =, diferente de imutaveis, os mutaveis assumem o valor da memoria e não o valor daquele imutavel
# Mas utilizando copy, copiamos ela que nem em imutaveis

lista = [12, "olá", True, 2.3, "Bolsonaro", []]
print(lista)
print(lista[0])
print(type(lista[5]))
lista[1] = lista[1].upper()
print(lista)

print(10 * "----")

del lista[0]  # Delemos qual indice queremos
lista.append(50)  # adicionamos tal coisa
lista.pop()  # dentro dos parenteses podemos colocar o indice para remover / caso n tenha nenhum o ultimo é removido
lista.append(60)
ultima_removida = lista.pop(2)
print(lista)
print(ultima_removida)

print(10 * "----")

lista.insert(0, 5)  # Adicione um item ao indice (primeiro digito), o item é o (segundo digito)
print(lista)
lista.clear()  # Apaga toda a lista
print(lista)

print(10 * "----")

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b  # Soma duas listas
lista_d = ["Bolsonaro"]
print(lista_c)
lista_a.extend(lista_d)  # Mexe diretamente extendendo a lista A
print(lista_a)

print(10 * "----")

teste_lista = ["andre", 19]
teste_lista_2 = teste_lista.copy()
teste_lista[0] = 18
print(teste_lista_2)