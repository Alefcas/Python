from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}\nO ângulo de {} tem o COSSENO de {:.2f}\nO ângulo de {} tem a TANGENTE de {:.2f}'.format
      (angulo, seno, angulo, cosseno, angulo, tangente))