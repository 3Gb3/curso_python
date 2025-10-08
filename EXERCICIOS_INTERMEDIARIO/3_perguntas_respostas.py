# Exercicio para criar um sistema de perguntas e respostas
# Primeira vez mexendo em dicionario dentro de listas
# Utilizei o ChatGpt no modo Estudar, para entender como navegar nos dicionarios dentro de uma lista

perguntas = [
    {'pergunta': 'Quanto é 12+8?',
     'opcoes': ['16', '20', '23', '22'],
     'resposta': '20'
    },
    {'pergunta': 'Quanto é 15+8?',
     'opcoes': ['23', '14', '19', '65'],
     'resposta': '23'
    },
    {'pergunta': 'Quanto é 12*9?',
     'opcoes': ['108', '110', '109', '120'],
     'resposta': '108'
    }
]

while True:
    pontos = 0
    controle_break = False
    for pergunta in perguntas:
        print(pergunta['pergunta'])
        for i, opcao in enumerate(pergunta['opcoes']):
            print(f'[{i}] {opcao}')
        resposta = input('Qual a alternativa correta? ')
        try:
            resposta_int = int(resposta)
        except ValueError:
            print('Digite um número por favor')
            break
        if resposta_int >= 0 and resposta_int <= len(pergunta['opcoes']):
            if pergunta['opcoes'][resposta_int] == pergunta['resposta']:
                print('Acertouuu')
                pontos += 1
            else:
                print('Errado')
        else:
            print('Digite algo entre 0 e 3')
            controle_break = True
            break
    if controle_break:
        break
    print(f'Você acertou {pontos} de {len(perguntas)}')
    break