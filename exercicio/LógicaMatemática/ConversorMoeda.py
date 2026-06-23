r = float(input('Quanto dinheiro Você tem na carteira? R$'))
dolar = r/ 5.81
euro = r/6.70
peso = r*187.70
print('Com R${:.2f} você pode comprar:\n'
      'US${:.2f}\n'
      'EUR${:.2f}\n'
      'ARS${:.2f}\n'.format(r, dolar, euro, peso))
