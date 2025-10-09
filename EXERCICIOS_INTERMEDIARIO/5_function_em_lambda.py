# Transformar as funções soma e multiplicar para lambda

def executa(funcao, *args):  # Função que executa funções
    return funcao(*args)

def soma(x, y):  # Soma Padrão
    return x + y

print(
    executa(
        lambda x, y: x + y, 2, 3  # Cria uma função anonima e passa isso para o executor, onde ele recebe os argumentos e retorna o valor
)
)


def criar_multiplicador(multiplicador):  # Multiplicador padrão
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplicar = executa(lambda n: lambda m: n * m, 2)  # Cria uma variavel onde tem como padrão o multiplicador 2

print(duplicar(3))  # Passamos o segundo argumento, então fazemos 2 * 3

# BONUS
# Somar todos os numeros informados

somar = executa(lambda *args: sum(args), 0, 2, 3, 4, 5, 6, 7)  # Passamos a função que faz a soma de todos os números
print(somar)