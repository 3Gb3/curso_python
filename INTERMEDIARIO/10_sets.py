# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

l1 = [1, 3, 3, 5, 5, 4, 2, 1]
l1 = list(set(l1))
print(l1)

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Luiz')
s1.update('Bom')
s1.update(('Teste', 1, 2, 3, 4))
print(s1)
s1.discard('B')
s1.discard('o')
s1.discard('m')
# s1.clear()
print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença (difference)- Itens presentes apenas no set da esquerda
# diferença simétrica ^(symmetric_difference) - Itens que não estão em ambos
print()
s2 = {1, 2, 3}
s3 = {2, 3, 4}
s4 = s2 | s3
s5 = s2 & s3
s6 = s2 - s3
s7 = s2 ^ s3  # Ao meu ver, um intersection ao contrario
print(s4)
print(s5)
print(s6)
print(s7)