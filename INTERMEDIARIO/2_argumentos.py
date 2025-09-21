"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def teste(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


teste(1, 2, 3)
teste(1, y=3, z=2)

print(1, 2, 3, sep='-')

"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)