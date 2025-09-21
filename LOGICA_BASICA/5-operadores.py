# Operadores lógicos
# and (e) Tudo deve ser verdadeiro
# or (ou) Pelo menos um deve ser verdadeiro
# not (não) Inverte o valor lógico / False = True / True = False

# Operadores Lógicos V2
# in (entre) 
# not in (não entre)

# Exemplos com os operadores lógicos
# And
senha = input("Digite a senha: ")
idade = input("Digite sua idade: ")
senha_correta = "123456"
idade_n = int(idade)

if idade_n >= 18 and senha_correta == senha:
    print("Acesso permitido")
else:
    print("Acesso negado")
# Or
if idade_n < 18 or senha_correta != senha:
    print("Entrada Teste")
# Not
if not senha:
    print("Acesso Negado")
elif senha != senha_correta:
    print("Acesso Negado")
elif senha == senha_correta:
    print("Acesso Permitido")

# Variaveis usadas para o IN e NOT IN
nome = input("Digite seu nome: ")
encontre = input("Digite a letra que deseja localizar: ")
# In
if encontre in nome:
    print(f"{encontre} está em {nome}")
# Not In
if encontre not in nome:
    print(f"{encontre} não está em {nome}")