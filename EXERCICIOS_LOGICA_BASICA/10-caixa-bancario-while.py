# 🏦 Crie um programa que simule um caixa eletrônico:
# O usuário começa com um saldo inicial de R$ 1000.
# O programa deve mostrar um menu repetidamente:
# Se escolher 1, mostra o saldo.
# Se escolher 2, pede um valor e adiciona ao saldo.
# Se escolher 3, pede um valor e:
# Se tiver saldo suficiente, desconta
# Se não tiver saldo, mostra mensagem de erro
# Se escolher 4, o programa termina.
# Se digitar qualquer outra coisa, mostra "Opção inválida" e volta ao menu.

dinheiro_na_conta = 1000
while True:
    print("\n🏦 Banco do Gb")
    print("💰 [1] Saldo")
    print("➕ [2] Depositar")
    print("➖ [3] Sacar")
    print("🚪 [4] Sair")

    escolha = input("👉 Escolha uma opção: ")
    escolha_int = escolha.isdigit()

    if escolha_int:
        escolha_real = int(escolha)
    else:
        print("⚠️ Opção inválida! Digite um número de 1 a 4.")
        continue

    try:
        if escolha_real == 1:
            print(f"💳 Seu saldo é R${dinheiro_na_conta:.2f}")

        elif escolha_real == 2:
            depositar = input("💵 Quanto você gostaria de depositar: ")
            depositar_float = float(depositar)
            if depositar_float <= 0:
                print("⚠️ Valor incorreto, digite um valor positivo!")
                continue
            else:
                dinheiro_na_conta += depositar_float
                print(f"✅ Depósito de R${depositar_float:.2f} realizado!")
                print(f"📊 Novo saldo: R${dinheiro_na_conta:.2f}")

        elif escolha_real == 3:
            sacar = input("💸 Digite o valor que você deseja sacar: ")
            sacar_float = float(sacar)
            if sacar_float > dinheiro_na_conta:
                print("❌ Saldo insuficiente!")
                continue
            elif sacar_float <= 0:
                print("⚠️ Valor de saque indevido, tente novamente!")
                continue
            else:
                dinheiro_na_conta -= sacar_float
                print(f"✅ Saque de R${sacar_float:.2f} realizado com sucesso!")
                print(f"📊 Novo saldo: R${dinheiro_na_conta:.2f}")

        elif escolha_real == 4:
            print("👋 Obrigado por usar o Banco Gb!")
            break

        else:
            print("⚠️ Opção inválida! Escolha entre 1 e 4.")
            continue

    except ValueError:
        print("⚠️ Valor inválido! Digite apenas números.")
        continue