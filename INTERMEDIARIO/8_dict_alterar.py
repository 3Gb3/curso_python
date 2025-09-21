# Manipular o dict

pessoa = {}  # Dict Vazio

chave = 'nome'  # Variavel para atribuirmos no dict
pessoa[chave] = 'Gabriel'

print(pessoa)

pessoa['idade'] = 18
pessoa[chave] = 'Carlos'
del pessoa['idade']

for teste in pessoa:
    print(f'{teste}: {pessoa[teste]}')

if pessoa.get('idade') is None:
    print('Sem idade')
else:
    print(f'A idade é {pessoa["idade"]}')