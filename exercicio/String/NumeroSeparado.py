#programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Alef Castro
# 12/05/2026

num = int(input("Digite um Numero entre 0 e 9999: "))
n = str(num)
print("Analisando o numero...")

print("Unidade: {}".format(n[0]))
print("Dezena: {}".format(n[1]))
print("Centena: {}".format(n[2]))
print("Milhar: {}".format(n[3]))
