# Programa que lê o nome de uma pessoa e diga se ela tem 'SILVA'no nome
# Alef Castro
# 25/06/2026

nome = str(input("Qual o seu nome Completo: ")).strip()
print("Seu nome tem SILVA? {}".format('Silva' in nome.lower()))
