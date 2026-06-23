#programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
# Alef Castro
# 12/05/2026

nome = str(input("Qual cidade você nasceu? ")).strip()
print(nome[:5].lower() == 'santo')

