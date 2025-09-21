lista = ['Maria', 'Eduardo', 'Helena', 2, 3, 4]
a, b , c, *_, ultimo = lista

lista_desempacotar = a, b, c, ultimo
resto_lista = _
lista_lista = list(lista_desempacotar)

print(lista_desempacotar)
print(resto_lista)
print(lista_lista)

for nome in lista:
    print(nome, end= ' ')

print(" ")

print(*lista)