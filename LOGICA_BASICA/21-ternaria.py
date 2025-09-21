"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = '1'

# variavel = 'Verdadeiro' if condicao else 'Falso'

# print(variavel)

digito = 9
novo_digito = 0 if digito > 9 else digito

print(novo_digito)

print('Valor' if False else 'Outro valor' if False else 'Fim')