# Imprecisão de ponto flutuante
# Double-precision floating-point format IEEE 754
# Mais sobre o tema:
# https://en.wikipedia.org/wiki/Double-precision_floating-point_format
# https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

import decimal  # Importa o módulo 'decimal' para trabalhar com números decimais com alta precisão

# --- Exemplo com floats normais (padrão IEEE 754) ---
numero_1 = 0.1          # Define um número de ponto flutuante (float)
numero_2 = 0.7          # Outro número float
numero_3 = numero_1 + numero_2  # Soma de dois floats

print(numero_3)         # Exibe o resultado da soma -> normalmente dá 0.7999999999999999 (imprecisão)
print(f'{numero_3:.2f}')  # Formata para 2 casas decimais (0.80), mas apenas visualmente
print(round(numero_3, 2)) # Arredonda para 2 casas decimais de forma numérica -> 0.8

print("----" * 10)      # Linha de separação visual

# --- Exemplo com o módulo Decimal (alta precisão) ---
# Quando usamos Decimal, evitamos as imprecisões do formato binário do float
numero_1 = decimal.Decimal('0.1')  # Cria um Decimal a partir de uma string (mantém precisão exata)
numero_2 = decimal.Decimal('0.7')  # Outro Decimal
numero_3 = numero_1 + numero_2     # Soma exata sem erro de representação

print(numero_3)         # Exibe o resultado -> 0.8 de forma precisa
print(f'{numero_3:.2f}')  # Também formata para 2 casas decimais (continua 0.80)
print(round(numero_3, 2)) # Arredonda (mas nesse caso não há diferença, já é exato)