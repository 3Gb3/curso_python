"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Gabriel Schwingel'
outra_variavel = f'{string[:7]}amos{string[7:]}'
print(string)
print(outra_variavel)
print(string.zfill(20))

print(10 * "----")
#  Métodos de String / apenas alguns dos métodos mais utilizados

texto = "  python é TOP!  "

print(texto.strip())         # Remove espaços -> "python é TOP!"
print(texto.upper())         # "  PYTHON É TOP!  "
print(texto.lower())         # "  python é top!  "
print(texto.replace("TOP", "bom"))  # "  python é bom!  "
print(texto.count("o"))      # Conta quantos 'o' tem
print(texto.split())         # ['python', 'é', 'TOP!']