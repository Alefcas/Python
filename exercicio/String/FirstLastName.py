#Programa que lê o nome completo de uma pessoa, mostrando em seguida o primeiro e
# o último nome separadamente!
# 31/08/2026

nome = str(input("Escreva seu nome completo: ")).strip()
n = nome. split()
print("\033[1;35mSeu primeiro nome é \033[4m{}\033[m".format(n[0]))
print("\033[1;32mSeu último nome é \033[4m{}\033[m".format(n[len(n)-1]))