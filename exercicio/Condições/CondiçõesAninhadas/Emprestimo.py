# Programa que aprova o empréstimo bancário para a compra de uma casa,
#perguntando o valor da casa, Salário do comprador e em quantos ANOS vai
#pagar. A prestção mensal não pode exceder 30% do salário. Senão terá o
#empréstimo NEGADO.
# Alef Castro
# 10/09/2026

print("\033[1;35m--FAÇA SEU EMPRÉSTIMO AQUI--\033[m")
casa = float(input("Valor da Casa: R$"))
salario = float(input("Salário do Comprador: R$"))
anos = int(input("Quantos anos de financiamento: "))
prestacao = casa / (anos * 12)

print("Para pagar a casa de R${:.2f} em {} anos.".format(casa,anos), end="")
print(" A prestação será de R${:.2f}".format(prestacao))
if prestacao > salario*0.3:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo CONCEDIDO!")
