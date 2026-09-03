# Programa 'pensa' em um numero entre 0 e 5 e peça para o usuario adivinhar!
# Alef Castro
# 03/09/2026
from random import randint
from time import sleep

pc = randint(0, 5)
print("Pensando em um número....")
player =  int(input("Qual o número que eu pensei? "))
print("Processando resultado...")
sleep(3)
if player == pc:
    print("PARABENS!! Acertou o número!")
else:
    print("ERROU! O número escolhido foi {}". format(pc))