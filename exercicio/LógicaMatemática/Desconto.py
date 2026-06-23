valor = float(input('Qual o valor do produto?R$'))
valor_f = valor - (valor*5/100)
print ("O valor de tal produto é R${:.2f}. Mas com o desconto de 5%, o preço fica R${:.2f}".format(valor, valor_f))
