# 🛒 Programa de lista de compras simples com opções para adicionar, remover e mostrar itens
# 🚫 Tratamento para não deixar o programa quebrar com índices inválidos

lista_compras = []  # Inicializa a lista de compras vazia

import os  # Importa módulo para comandos do sistema, usado aqui para limpar a tela

while True:  # Loop infinito para manter o programa rodando até o usuário escolher sair
    print("🍿 Bem vindo ao mercadinho do Gb")  # Saudação inicial
    print("🛍️ Suas escolhas são as seguintes: ")  # Menu de opções para o usuário
    escolha = input("[1]Adicionar ➕ \n[2]Remover ➖ \n[3]Listar 📋 \n[4]Sair 🚪\n❓ Oque Deseja Realizar: ")

    try:
        escolha_int = int(escolha)  # Tenta converter a escolha para um número inteiro
    except:
        print("⚠️ Digite um número válido, por favor!")  # Se não for número, mostra aviso
        continue  # Volta pro começo do loop para pedir de novo

    # Se a escolha foi 1, entra na opção de adicionar itens
    if escolha_int == 1:
        os.system("cls")  # Limpa a tela para ficar mais organizado (funciona no Windows)
        adicionar = input("📝 O que deseja adicionar na lista? ").strip().lower()
        if adicionar not in lista_compras:  # Verifica se esse item já está na lista
            # Pega o texto digitado, remove espaços extras e transforma em minúsculas para uniformizar
            lista_compras.append(adicionar)  # Adiciona o item à lista
        else:
            os.system("cls")
            print("⚠️ Esse item já está na sua lista!\n")
            continue

        print(f"✅ Sua nova lista de compras é: ")
        # Mostra a lista atualizada, enumerando os itens (índice + 1 para ficar mais humano)
        if lista_compras:  # Verifica se a lista é vazia ou não
            for indice, nomes in enumerate(lista_compras):
                print(f"[{indice + 1}] {nomes}")
            print("")  # Linha em branco para espaçamento
        else:
            print("⚠️ Sua lista está vazia\n")
        continue  # Volta ao menu principal

    # Se a escolha foi 2, entra na opção de remover itens
    elif escolha_int == 2:
        os.system("cls")  # Limpa a tela antes de mostrar as opções
        if lista_compras:  # Verifica se a lista não está vazia
            indice_nome = input("❓ Deseja remover pelo número ou nome? (digite numero ou nome): ").strip().lower()
            # Pergunta se quer remover pelo índice ou pelo nome do produto

            if indice_nome == "numero":  # Remover por índice numérico
                print(f"🛒 Sua lista de compras é: ")
                for indice, nomes in enumerate(lista_compras):
                    print(f"[{indice + 1}] {nomes}")
                print("")
                remover_i = input("🗑️ Qual número remover da lista? ").strip()
                try:
                    remover_int = int(remover_i)  # Converte a entrada para inteiro
                    del lista_compras[remover_int - 1]  # Remove o item da lista (ajustando índice)
                    os.system("cls")  # Limpa a tela para mostrar o resultado
                    print(f"✅ Sua nova lista de compras é: ")
                    for indice, nomes in enumerate(lista_compras):
                        print(f"[{indice + 1}] {nomes}")
                    print("")
                    continue
                except IndexError:  # Se o índice estiver fora do intervalo da lista
                    os.system("cls")
                    print(f"⚠️ Número {remover_int} fora da lista, tente novamente.")
                    continue
                except ValueError:  # Se o usuário não digitou um número
                    print("⚠️ Por favor, digite um número válido.")
                    continue

            elif indice_nome == "nome":  # Remover por nome do item
                print(f"🛒 Sua lista de compras é: ")
                for indice, nomes in enumerate(lista_compras):
                    print(f"[{indice + 1}] {nomes}")
                print("")
                remover_n = input("🗑️ O que deseja remover da lista? ").strip().lower()
                os.system("cls")  # Limpa antes de mostrar a resposta
                if remover_n in lista_compras:  # Verifica se o nome existe na lista
                    lista_compras.remove(remover_n)  # Remove o item pelo nome
                    print(f"✅ Sua nova lista de compras é: ")
                    for indice, nomes in enumerate(lista_compras):
                        print(f"[{indice + 1}] {nomes}")
                    print("")
                    continue
                else:
                    print("⚠️ Esse nome não está na lista.")
                    continue
            else:  # Caso não digite "nome" ou "numero"
                os.system("cls")
                print("❌ Por favor, digite 'nome' ou 'numero'.")
                continue
        else:  # Se a lista estiver vazia, não tem o que remover
            os.system("cls")
            print("⚠️ A lista está vazia, nada para remover.")
            continue

    # Se a escolha foi 3, lista todos os itens da lista de compras
    elif escolha_int == 3:
        os.system("cls")  # Limpa tela antes de mostrar a lista
        print(f"📋 Sua lista de compras é: ")
        if not lista_compras:  # Se a lista estiver vazia
            print("⚠️ Sua lista está vazia\n")
            continue
        else:
            # Mostra todos os itens enumerados, com espaçamento entre eles
            for indice, produtos in enumerate(lista_compras):
                print(f"[{indice + 1}] {produtos}")
            print("")
            continue

    # Se a escolha foi 4, sai do programa
    elif escolha_int == 4:
        os.system("cls")
        print("👋 Obrigado por usar as listas do Gb! Até a próxima!")
        break  # Sai do loop e encerra o programa

    else:  # Caso digite número diferente das opções
        print("⚠️ Digite uma das opções acima")
        continue