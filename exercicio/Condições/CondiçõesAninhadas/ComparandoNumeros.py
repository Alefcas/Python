#Programa que leia dois numeros inteiros e compare-os qual deles é maior ou menor
#Alef Castro
#11/09/2026
print("===COMPARAÇÃO DE NÚMEROS===")
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
if a > b:
    print("O primeiro valor é maior!")
elif b > a:
    print("O segundo valor é maior!")
else:
    print("Não existe maior, os dois são iguais!")