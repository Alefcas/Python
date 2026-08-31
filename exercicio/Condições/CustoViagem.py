# Programa que pergunte a distância de uma viagem em Km. O preço da passagem é R$0,50 por Km para
# viagens de até 200Km e R$0,45 de viagens mais longas.
# Alef Castro
# 31/08/2026

viagem = float(input("Qual a distância da viagem: "))
if viagem <= 200:
    print("Para a viagem de {}km, pagará R${:.2f}".format(viagem, viagem*0.50))
else:
    print("Para a viagem de {}km, pagará R${:.2f} (Promoção)".format(viagem, viagem*0.45))