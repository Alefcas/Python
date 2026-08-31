# Programa que lê a velocidade de um carro. SE ultrapassar 80Km/h mostre uma mensagem de MULTA.
# A multa vai custar R$7,00 por cada KM acima do limite.
# Alef Castro
# 31/08/2026

velocidade =  int(input("Digite a velocidade(Km/h) do Veículo: "))
multa = (velocidade-80) * 7
if velocidade > 80:
    print("MULTADO!!!, excedeu o limite de velocidade!")
    print("Velocidade: {}km/h | Valor da Multa: R${}".format(velocidade, multa))
else:
    print("Não foi multado!")