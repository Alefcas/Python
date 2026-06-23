from math import hypot
#importei somente o hypot, pra conseguir calcular de forma prática.
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa tem seu comprimento: {:.2f}'.format(hip))