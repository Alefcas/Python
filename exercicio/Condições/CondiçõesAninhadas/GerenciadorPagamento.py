#Programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
#á vista dinheiro/cheque = 10% desconto | á vista no cartão: 5% desconto |
#2x no cartão: preço formal | 3x ou mais no cartão:20% de juros
#Alef Castro
#18/09/2026
preco = float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO")
print("[1] á vista dinheiro/cheque\n"
      "[2] á vista cartão\n"
      "[3] 2x no cartão\n"
      "[4] 3x ou mais no cartão")
opc = int(input("Qual é a opção? "))
if opc == 1:
    total = preco - (preco * 0.1)
    print("10% de desconto")
elif opc == 2:
    total = preco - (preco * 0.05)
    print("(5% de desconto)")
elif opc == 3:
   total = preco
   parcela = total/2
   print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS".format(parcela))
elif opc == 4:
    totalparc = int(input("Quantas parcelas? "))
    total = (preco * 0.2) + preco
    parcela = total / totalparc
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(totalparc,parcela))
else:
    total = preco
    print("Opção Invalida de pagamento. Tente Novamente")
print("Sua compra de R${:.2f} vai custar R${:.2f}".format(preco, total))