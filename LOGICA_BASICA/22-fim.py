import time
import sys
import platform

# 🎨 Cores ANSI estilo hacker
VERDE = "\033[92m"
RESET = "\033[0m"
NEGRITO = "\033[1m"

# Detecta o sistema para som
IS_WINDOWS = platform.system() == "Windows"
if IS_WINDOWS:
    import winsound

def beep(freq=1500, dur=8):
    """Som de terminal rápido"""
    if IS_WINDOWS:
        winsound.Beep(freq, dur)  # Beep no Windows
    else:
        sys.stdout.write("\a")    # Bell no Linux/Mac
        sys.stdout.flush()

def escrever_hacker(texto, delay=0.01, som=True):
    """Escreve rápido com som estilo hacker"""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char not in [" ", "\n"] and som:
            beep()
        time.sleep(delay)
    print()

def loading_animacao():
    """Animação de LOADING... com pontos piscando"""
    sys.stdout.write(VERDE + "LOADING" + RESET)
    sys.stdout.flush()
    for _ in range(6):  # 6 ciclos de carregamento
        sys.stdout.write(".")
        sys.stdout.flush()
        beep(1000, 20)
        time.sleep(0.3)
    print("\n")  # Quebra de linha depois do loading

def acesso_concedido():
    """Mensagem final piscando estilo terminal"""
    for _ in range(6):  # pisca 3x
        sys.stdout.write(f"\r{NEGRITO}{VERDE}[ACESSO CONCEDIDO]{RESET}   ")
        sys.stdout.flush()
        beep(2000, 30)
        time.sleep(0.3)
        sys.stdout.write("\r                     ")  # apaga
        sys.stdout.flush()
        time.sleep(0.3)
    print(f"\r{NEGRITO}{VERDE}[ACESSO CONCEDIDO]{RESET}")  # fixo no final

def mensagem_hacker():
    """Mostra mensagem estilo terminal hacker"""
    borda = "=" * 80
    
    mensagem = (
        f"{VERDE}Chegamos finalmente ao fim da primeira secção né Gb!\n"
        f"Aprendemos como fazer um gerador de CPF válido KKKKKKK.\n\n"
        f"Nessa época (22/07/2025) eu achei isso muito foda!\n"
        f"Vamos ver o que iremos fazer a mais até o final desse curso de Python...\n\n"
        f"Eu vou voltar para ler isso aqui somente quando acabar tudo do curso.\n"
        f"E no final de toda secção vai ter uma mensagem dessas.\n\n"
        f"Mas vamos lá Gb, confio que tu vai ter forças pra aguentar tudo que está por vir\n"
        f"e quero muito ver o grande programador que tu vai se tornar!\n\n"
        f"Abraços do Gb de 22/07/2025 às 16:54\n"
        f"{RESET}"
    )

    # 1️⃣ Mostra LOADING... com pontos piscando
    loading_animacao()
    
    # 2️⃣ Mostra borda e mensagem digitada
    print(VERDE + borda + RESET)
    escrever_hacker(mensagem, delay=0.01, som=True)
    print(VERDE + borda + RESET)
    
    # 3️⃣ Finaliza com ACESSO CONCEDIDO piscando
    acesso_concedido()

if __name__ == "__main__":
    mensagem_hacker()