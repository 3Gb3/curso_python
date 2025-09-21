# str - int - float - bool

# Variáveis
# Variáveis só podem começar com letras ou underscore (_)
nome = "João"
idade = 30
altura = 1.75
ativo = True

# Exibindo as variáveis
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Ativo:", ativo)

# Conversão de tipos
print(int("1") + 2)

# Strings vazias são consideradas False
print(bool(""))  # False
print(bool(" "))  # True (espaço em branco é considerado True)

# Operadores lógicos
adicao = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 3
divisao_inteira = 10 // 3
modulo = 10 % 3  # Módulo (resto da divisão)
exponenciacao = 10 ** 3
print("Adição:", adicao)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão inteira:", divisao_inteira)
print("Módulo:", modulo)
print("Exponenciação:", exponenciacao)

# Concatenação de strings
juntar = "10" + "5"  # Concatenação de strings
print("Juntar:", juntar)
juntar_vezes = "10" * 5  # Repetição de strings
print("Juntar vezes:", juntar_vezes)