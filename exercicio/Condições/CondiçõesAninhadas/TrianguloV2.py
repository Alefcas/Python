# Programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
# e diga qual o tipo de triangulo: Equilátero, Isósceles e Escaleno.
# Alef Castro
# 13/09/2026
a = float(input("Prineira Reta: "))
b = float(input("Segunda Reta: "))
c = float(input("Terceira Reta: "))

if (a + b) > c and (b + c) > a and (c + a) > b:
    print("\033[1;33mÉ possivel SIM fazer um triângulo!\033[m")

    if a == b and b == c:
        print("É um triângulo EQUILÁTERO")
    elif a == b and b != c or b == c and c != a or c == a and a != b:
        print("É um triângulo ISÓSCELES")
    else:
        print("É um triângulo ESCALENO")

else:
    print("\033[1;35mNÃO é possivel formar um triângulo!\033[m")