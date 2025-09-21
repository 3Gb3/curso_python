#  Constante = variaveis que nunca mudam o valor
#  Muitas codições dentro de um IF (RUIM)
#    <- Contagem de complexidade (RUIM)
#  Como deixar o codigo mais legivel para eu mesmo ou outros progamadores

velocidade = 61  # Velocidade atual do carro
local_carro = 101  # Local onde o carro está

#  Variaveis com capslock são "Constantes" entre os programadores
RADAR_1 = 60  # Velocidade maxima do radar 1
LOCAL_1 = 100  # Local do radar 1
RADAR_RANGE = 1  # Distancia que o radar 1 chega

#  Contratante quer que eu verifique se o carro está dentro do local que o radar atinge
#  E se o motorista passou da velocidade

velocidade_maior = velocidade > RADAR_1  # Se a velocidade for maior que o limite = True
local = (LOCAL_1 - RADAR_RANGE <= local_carro <= LOCAL_1 + RADAR_RANGE)  # Se o local do carro está no radar = True
carro_multado = local and velocidade_maior  # Carro multado se ambas as condições forem = True

if carro_multado:
    print("Motorista Multado")
else:
    print("Sem multas")