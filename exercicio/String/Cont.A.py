#programa que lê uma frase e mostre quantas vezes aparece a letra A e sua posição Inicial e final
# Alef Castro
# 25/06/2026

frase = str(input("Escreva sua Frase: ")).lower().strip()
print("A letra A apareceu {} vezes na frase.".format(frase.count('a')))
print("A primeira letra A apareceu na posição {}.".format(frase.find('a')+1))
print("A última letra A apareceu na posição {}".format(frase.rfind('a')+1))