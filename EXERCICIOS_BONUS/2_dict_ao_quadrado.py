#  Exercicio realizado do site:
#  https://www.machinelearningplus.com/python/python-exercises-beginner/
#  Q2: Generate Square Dictionary

dict = {}

tamanho_dict = input('Digite o tamanho do dict ao quadrado: ')

if tamanho_dict.isdigit():
    def gerar_dict_quadrado(a):
        for i in range(1, a + 1):
            dict[str(i)] = str(i * i)
        return dict

    print(gerar_dict_quadrado(int(tamanho_dict)))
else:
    print('Digite um número inteiro por favor')