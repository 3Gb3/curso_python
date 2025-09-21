# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy  # Usado para copia profunda, onde dados mutaveis param de ficar linkados um no outro no copy
# Se utiliza copy.deepcopy(conteudo) para fazer forma de dados mutaveis não linkarem entre dicionarios

teste = {'nome': 'Carlos'}

print(len(teste))
print(teste.keys())
print(teste.values())
print(teste.items())

teste.setdefault('idade', 'Sem Idade')  # Coloca algo para aparecer caso não tenha nada no 'idade'
print(teste['idade'])

teste2 = teste.copy()  # Aqui é o mesmo principio das listas, caso eu declare teste2 = teste, caso eu altere o valor de um deles ambos irão alterar

if teste.get('nome', False) is not False:  # Aqui ele tenta localizar o 'nome' dentro do dict, caso não encontre retorna False (por padrão é None)
    print('Tem o Nome')
else:
    print('Não tem nome')

print(10 * '----')

teste['sobre mim'] = 'Sou Brasileiro'
teste.pop('idade')  # Mesmo que del, mas em forma de .pop
print(teste)
teste.popitem()  # Apaga o ultimo item adicionado
print(teste)