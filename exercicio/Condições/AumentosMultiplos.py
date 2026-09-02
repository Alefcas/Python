# Programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# MAIOR que R$1250,00, calcule um aumento de 10%. MENOR ou IGUAL, o aumento é de 15%.
# Alef Castro
# 02/09/2026
salario = float(input("Qual o salario do funcionario? R$"))
if salario <= 1250.00:
    dez = salario * 1.15
    print("Quem ganhava R${:.2f} vai passar a ganhar R${:.2f}. ".format(salario, dez))
else:
    quinze = salario * 1.1
    print("Quem ganhava R${:.2f} vai passar a ganhar R${:.2f}. ".format(salario, quinze))