#Programa que leia o ano de nascimento e informe se ele ainda vai se alistar
#ao serviço militar, se é a hora exata ou se ja passou do tempo.
#Alef Castro
#11/09/2026
from datetime import date
atual = date.today().year
ano = int(input("Ano de Nascimento: "))
idade = atual - ano
print("Quem Nasceu em {} tem {} anos em {}.".format(ano,idade, atual))

if idade < 18:
    anof = 18 - idade #anof == Anos que Falta
    print("Ainda falta {} anos para o alistamento".format(anof))
    print("Seu alistamento será em {}.".format(ano + anof))
elif idade > 18:
    anop = idade - 18 #anop == Anos que Passou
    print("Você já deveria ter se alistado há {} anos".format(anop))
    print("Seu alistamento foi em {}.".format(ano - anop))
else:
    print("Você deve se alistar IMEDIATAMENTE!")