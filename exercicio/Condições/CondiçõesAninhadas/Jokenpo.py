# Programa que a máquina joga Jokenpo (pedra, papel e tesoura) com o usuario
# Alef Castro
# 14/09/2026
from random import randint
from time import sleep

pc = randint(0,2)
itens = ("Pedra", "Papel","Tesoura")

print("Suas Opções:\n[0] Pedra\n[1] Papel\n[2] Tesoura")
player = int(input("Qual a sua jogada?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("POO")
sleep(1)
print("\033[33m=\033[m"*30)
print("O computador escolheu {}".format(itens[pc]))
print("O Jogador escolheu {}".format(itens[player]))
print("\033[33m=\033[m"*30)
if pc == 0: # PEDRA
    if player == 0:
        print("EMPATE!")
    elif player == 1:
        print("JOGADOR GANHOU")
    elif player == 2:
        print("COMPUTADOR GANHOU")

elif pc == 1: # PAPEL
    if player == 0:
        print("COMPUTADOR GANHOU")
    elif player == 1:
        print("EMPATE")
    elif player == 2:
        print("JOGADOR GANHOU")

elif pc == 2: # TESOURA
    if player == 0:
        print("JOGADOR GANHOU")
    elif player == 1:
        print("COMPUTADOR GANHOU")
    elif player == 2:
        print("EMPATE")