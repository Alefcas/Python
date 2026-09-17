#Programa que leia um numero e faça a conversão para binario, octal ou hexadecimal
#seguindo a escolha do usuario.
#Alef Castro
#16/09/2026
print("\033[31m=\033[m"*30)
print("CONVERSOR DE BASES NUMERICAS")
print("\033[31m=\033[m"*30)
num = int(input("Qual o numero que deseja converter: "))
print("Em qual base deseja converter")
print("[1] Binário\n"
      "[2] Octal\n"
      "[3] Hexadecimal")
opc = int(input("Sua opção: "))
if opc == 1:
    print("{} na base Binario é exibido como: \033[35m{}".format(num, bin(num)[2:]))
                                                #[2:]- tira o indicador da base no print!
elif opc == 2:
    print("{} na base Octal é exibido como: \033[35m{}". format(num,oct(num)[2:]))
                                                # [2:]- tira o indicador da base no print!
elif opc == 3:
    print("{} na base Hexadecimal é exibifo como: \033[35m{}".format(num, hex(num)[2:]))
                                                # [2:]- tira o indicador da base no print!
else:
    print("\033[31m!!!Opção invalida!!!\033[m")