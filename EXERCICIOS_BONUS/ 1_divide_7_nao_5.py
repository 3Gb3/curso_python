#  Exercicio realizado do site:
#  https://www.machinelearningplus.com/python/python-exercises-beginner/
#  Q1. Find numbers Divisible by 7, not by 5




encontrados = []
print(f'O Programa ira do primeiro ao ultimo verificando qual divide por 7 e não por 5')
primeiro = input('Digite o numero inicial (int): ')
final = input('Digite o numero final (int): ')

while True:

    if not primeiro.isdigit() and not final.isdigit():
        print('Digite apenas números inteiros')
        break
    def verificar_divisor(a, b):
        for i in range(a, b):
            if (i % 7 == 0) and (i % 5 != 0):
                encontrados.append(i)
    verificar_divisor(int(primeiro), int(final))
    print(encontrados)
    break