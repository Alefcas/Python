# Programa que leia um ano qualquer e mostre se ele é bissexto.
# Alef Castro
# 01/09/2026
from datetime import date

ano = int(input("Qual ano quer analisar? (0 para analisar Ano atual)"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é Bissexto!". format(ano))
else:
    print("O ano {} NÃO é Bissexto!".format(ano))