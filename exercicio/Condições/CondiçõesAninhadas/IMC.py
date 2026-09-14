#Programa que calcule o Índece de Massa Corporal (IMC) e mostre seus status
#Alef Castro
#14/09/2026
print("\033[32m=== ÍNDICE DE MASSA CORPORAL ===\033[m")

peso = int(input("Qual o seu peso (kg): "))
altura = float(input("QUal a sua altura (m): "))
imc = peso / (altura * altura)

print("Seu Indice de Massa Corporal é {:.2f}".format(imc))
if imc < 18.5:
    print("Abaixo do Peso")
elif imc <= 25:
    print("Peso Ideal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")