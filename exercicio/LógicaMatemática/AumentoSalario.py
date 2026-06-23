salario_a = float(input('Qual o sálario do funcioário? R$'))
salario_f = salario_a + (salario_a*15/100)
print('O sálario do funcionário é R${:.2f}. Mas com 15% de aumento, ficará R${:.2f}'.format(salario_a, salario_f))