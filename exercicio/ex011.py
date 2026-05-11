larg = float(input('Qual a largura da sua parede?'))
alt = float(input('Qual a altura da sua parede?'))
area = alt * larg
litro = area / 2
print('A dimensão é {}x{} e a area é {:.2}m²\n'
      'Para pintar essa parede precisa de {}L de tinta'.format(larg, alt, area,litro))

