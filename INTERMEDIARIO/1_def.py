# Introdução às funções (def) em python
# Funções são trechos de código usados para replicar determinada ação ao longo do código
# Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico
# Por padrão, funções python retornam o valor None

def python():
    print("VIADAO")
python()

def parametros(a, b, c):  # Parametros
    print(a, b, c)

parametros(1, 2, 3)  # Argumentos

nome = "jorge"
def nome_usuario(usuario):
    print(usuario)

nome_usuario(nome)

idade_1 = 18
idade_2 = 25
def media_idades(i, i2):
    return (i + i2) / 2

print(media_idades(idade_1, idade_2))

def teste_nao_valor(naovalor="Sem Nome"):
    print(naovalor)

teste_nao_valor("Gabriel")