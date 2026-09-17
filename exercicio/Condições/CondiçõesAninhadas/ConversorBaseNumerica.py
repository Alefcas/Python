#Programa que leia um numero e faça a conversão para binario, octal ou hexadecimal
#seguindo a escolha do usuario.
#Alef Castro
#16/09/2026
num = int(input("Qual o numero que deseja converter: "))
print("Em qual base deseja converter")
print("[1] Binário\n"
      "[2] Octal\n"
      "[3] Hexadecimal")
opc = int(input("Sua opção: "))
if opc == 1:
    print("{} na base Binario é exibido como: {}".format(num, bin(num)[2:]))
elif opc == 2:
    print("{} na base Octal é exibido como: {}". format(num,oct(num)[2:]))
elif opc == 3:
    print("{} na base Hexadecimal é exibifo como: {}".format(num, hex(num)[2:]))
else:
    print("Opção invalida!")