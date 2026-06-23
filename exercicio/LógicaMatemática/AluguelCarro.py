print('='*20, 'Você alugou um carro!','='*20)
dia = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km foi rodado? '))
#Acima o banco de dados da questão.
pago = (dia * 60) + (km * 0.15)
#armazenei a váriavel pago aonde ja faz todo o calculo.
print('O total a pagar é de R${:.2f}'.format(pago))