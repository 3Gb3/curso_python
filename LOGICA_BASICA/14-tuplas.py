# Introdução ao empacotamento e desempacotamento
# *(nome variavel) é basicamente o resto da lista, utilizamos _ na comunidade para identificar que é o resto

nomes = ['Maria', 'Helena', 'Jorge']
nome1, nome2, nome3 = nomes
nome4, *_ = ['Maria', 'Helena', 'Jorge']

print(nome2)
print(nome4)

# Tupla = Lista Imutavel

idades = 18, 19 , 20
print(idades)
idades = (19, 19, 20)

# Podemos converter uma lista para tuple e vice-versa

nomes_imutavel = tuple(nomes)
nomes_mutavel = list(nomes)