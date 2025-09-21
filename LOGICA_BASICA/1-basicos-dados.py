# \r\n = CRLF
# \n = LF
# sep = oque vai ter na separação
# end = oque vai ter no final / padrão é \n

print(56, 46, sep='-', end='\r\n')
print(54, 78, sep='-', end='##')
print(54, 78, sep='-', end='\n')

# TIPAGEM DO PYTHON = Dinamica/Forte
# Tipagem Dinâmica = Não é necessário declarar o tipo da variável
# Tipagem Forte = Não é possível fazer conversões implícitas entre tipos

# string = texto

# escape
print("Gabriel \"Schwingel\"")

# r
print(r"Gabriel \"Schwingel\"")

# Metodo melhor = aspas duplas dentro de aspas simples ou vice-versa
print('Gabriel "Schwingel"')

# função type mostra o tipo da variável
print(type('Gabriel "Schwingel"'))
print(type(0.75))

# Boolean = True ou False
print(10 == 10)
print(10 == 11)