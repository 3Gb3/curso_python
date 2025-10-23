#  Exercicio realizado do site:
#  https://www.machinelearningplus.com/python/python-exercises-beginner/
#  Q6: Table Matrix

#  Matriz I x J

tamanho_matriz = input('Informe o tamanho da matriz exemplo: (3, 4): ')
tamanho_matriz = [item.strip() for item in tamanho_matriz.split(',')]

erro = False
for i in tamanho_matriz:
    if not i.isdigit():
        erro = True
        break

if erro or len(tamanho_matriz) != 2:
    print('Erro: Informe dois números válidos separados por vírgula!')
else:
    def criar_matriz(n, m):
        matriz = []

        for i in range(n):
            linha_nova = []
            for j in range(m):
                linha_nova.append(i * j)
            matriz.append(linha_nova)

        for linha in matriz:
            for elemento in linha:
                print(elemento, end=' ')
            print()

    criar_matriz(int(tamanho_matriz[0]), int(tamanho_matriz[1]))