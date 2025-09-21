# Exercicio para criar uma funcao que duplica, triplica e quadruplica o numero informado (basico, sem loops e essas coisas)

def multiplicar_vezes(vezes):
    def multiplicar_numero(numero):
        total = numero * vezes
        return total
    return multiplicar_numero

duplicar_numero = multiplicar_vezes(2)
triplicar_numero = multiplicar_vezes(3)
quadruplicar_numero = multiplicar_vezes(4)

duplicar = duplicar_numero(5)
triplicar = triplicar_numero(5)
quadruplicar = quadruplicar_numero(5)

print("Duplicado:", duplicar)
print("Triplicado:", triplicar)
print("Quadruplicado:", quadruplicar)