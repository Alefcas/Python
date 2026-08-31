# Programa que lê  um numero e mostre se é ÍMPAR ou PAR
# Alef Castro
# 31/08/2026

num = int(input("Escreva um numero inteiro: "))
if (num % 2) == 0:
    print(" O número {} é PAR".format(num))
else:
    print("O número {} é IMPAR".format(num))
