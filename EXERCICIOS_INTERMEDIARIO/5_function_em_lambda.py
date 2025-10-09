# Transformar as funções soma e multiplicar para lambda

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

print(
    executa(
        lambda x, y: x + y, 2, 3
)
)


def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplicar = executa(lambda n: lambda m: n * m, 2)

print(duplicar(3))

# BONUS
# Somar todos os numeros informados

somar = executa(lambda *args: sum(args), 0, 2, 3, 4, 5, 6, 7)
print(somar)