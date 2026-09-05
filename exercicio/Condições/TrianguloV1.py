# Programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# Alef Castro
# 03/09/2026
a = float(input("Prineira Reta: "))
b = float(input("Segunda Reta: "))
c = float(input("Terceira Reta: "))

if (a + b) > c and (b + c) > a and (c + a) > b:
    print("\033[1;33;40mÉ possivel SIM fazer um triângulo!\033[m")
else:
    print("\033[1;45mNÃO é possivel formar um triângulo!\033[m")