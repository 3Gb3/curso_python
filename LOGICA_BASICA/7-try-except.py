# Introdução ao try/except
# try = tenta executar o codigo
# except = ocorreu algum erro ao tentar executar

numero_str = input("Digite um número que eu irei dobrar: ")  # Número em str

try:  # Tenta executar o codigo de transformar em float
    numero_float = float(numero_str)  # Caso não seja um número retorna o except
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
except:  # Mostra o erro ao usúario
    print("Parece que você não digitou um numero, tente novamente.")