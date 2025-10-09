# Exercicio para criar um sistema de perguntas e respostas
# Primeira vez mexendo em dicionario dentro de listas
# Utilizei o ChatGpt no modo Estudar, para entender como navegar nos dicionarios dentro de uma lista

perguntas = [  # Aqui temos o sistema das perguntas
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
    controle_break = False  # Caso True faz o break final ser ativado
    for pergunta in perguntas:  # Percorre cada dicionario
        print(pergunta['pergunta'])
        for i, opcao in enumerate(pergunta['opcoes']):  # Adicionamos um indice para cada opção
            print(f'[{i}] {opcao}')
        resposta = input('Qual a alternativa correta? ')
        if resposta.isdigit():
            resposta_int = int(resposta)
        else:
            print('Digite um numero por favor')
            controle_break = True  # Atualiza para True o controle de break
            break
        if resposta_int >= 0 and resposta_int <= len(pergunta['opcoes']):  # Ver se está entre 0 e 3
            if pergunta['opcoes'][resposta_int] == pergunta['resposta']:  # Navega dentro da lista
                print('Acertouuu')
                pontos += 1
            else:
                print('Errado')
        else:
            print('Digite algo entre 0 e 3')
            controle_break = True  # Atualiza para True o controle de break
            break
    if controle_break:  # Caso tenha um erro, quebra o codigo não mostrando os pontos do usuario
        break
    print(f'Você acertou {pontos} de {len(perguntas)}')
    break