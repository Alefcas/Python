#Prgrama que leia o ano de nascimentode um atleta e mostre sua categoria
#Alef Castro
#13/09/2026
from datetime import date
print("\033[36m=== CONFEDERAÇÃO NACIONAL DE NATAÇÃO ===\033[m")
atual = date.today().year
ano = int(input("Qual o ano de Nascimento do Atleta: "))
categoria = atual - ano
print("Seu atleta tem {} anos".format(categoria))

if categoria <= 9:
    print("MIRIM")
elif categoria <= 14:
    print("INFANTIL")
elif categoria <= 19:
    print("JÚNIOR")
elif categoria <= 25:
    print("SÊNIOR")
else:
    print("MASTER")