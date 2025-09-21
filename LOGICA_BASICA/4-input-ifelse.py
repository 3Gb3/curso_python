nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")

idade_n = int(idade)

print(f"Olá, {nome}! Você tem {idade_n} anos.")

# IF / ELIF / ELSE
# Se / Se não se / Senão
# Operadores
# > maior que
# < menor que
# >= maior ou igual que
# <= menor ou igual que
# == igual a
# != diferente de

if idade_n < 18:
    print("Você é menor de idade.")
elif idade_n < 60:
    print("Você é adulto.")
else:
    print("Você é idoso.")

print("Obrigado por participar!")