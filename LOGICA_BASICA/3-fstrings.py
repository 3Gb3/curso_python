# F Strings é basicamente uma forma de formatar strings de maneira mais simples e legível.
# Exemplo de uso de f-strings
nome = "João"
idade = 30
mensagem = f"Olá, meu nome é {nome} e eu tenho {idade} anos."
print(mensagem)
# F Strings também permitem expressões dentro das chaves
altura = 1.75
mensagem_com_altura = f"{mensagem} Minha altura é {altura:.1f} metros."  # Isso faz aparecer apenas uma casa decimal
print(mensagem_com_altura)
# Caso queira ver o valor da variavel dentro da f-string
print(f"Qual seu nome? {nome=} e sua idade? {idade=}")  # Isso vai mostrar o nome e idade com o nome da variável

# Format
# A função format também pode ser usada para formatar strings
mensagem_formatada = "Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem_formatada)
mensagem_formatada_2 = "Olá, meu nome é {0} e eu tenho {1} anos.".format(nome, idade)
print(mensagem_formatada_2)
mensagem_formatada_3 = "Olá, meu nome é {nome} e eu tenho {idade} anos.".format(nome=nome, idade=idade)
print(mensagem_formatada_3)
# F Strings são mais recomendadas por serem mais legíveis e fáceis de usar