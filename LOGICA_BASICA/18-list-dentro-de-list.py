# Lista de listas e seus índices
# Temos uma lista 'salas' e, dentro dela, listas que representam cada sala com seus alunos

salas = [
    # Índices dos elementos dentro da sala
    # 0        1
    ['Maria', 'Helena', ],  # Sala 0
    # 0
    ['Elaine', ],           # Sala 1
    # 0       1       2           3 (que é uma TUPLA)
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40) ],  # Sala 2
]

# Exemplos de acessos diretos:
# print(salas[1][0])   -> Pega "Elaine" (sala 1, posição 0)
# print(salas[0][1])   -> Pega "Helena" (sala 0, posição 1)
# print(salas[2][2])   -> Pega "Eduarda" (sala 2, posição 2)
# print(salas[2][3][3]) -> Pega "30" (dentro da TUPLA que está na posição 3 da sala 2)

# Percorrendo cada sala na lista de salas
for sala in salas:
    print(f'A sala é {sala}')  # Exibe a lista completa daquela sala

    # Percorrendo cada aluno (ou elemento) dentro da sala
    for aluno in sala:
        print(aluno)  # Exibe cada aluno individualmente