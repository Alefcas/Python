# Programa que lê o nome de uma pessoa e diga se ela tem 'SILVA'no nome
# Alef Castro
# 25/06/2026

nome = str(input("\033[30;33mQual o seu nome Completo: \033[m")).strip()
print("Seu nome tem SILVA? {}".format('Silva' in nome.lower()))
