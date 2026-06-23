#Programa didatico para aprender sobre manipulação de código.
# Alef Castro
#04/28/2026 12h31

nome = str(input("Qual o seu nome? ")).strip()
print("Analisando seu nome...")
print("seu nome em maiusculas é: {}".format(nome.upper()))
print("seu nome em Minusculas é: {}".format(nome.lower()))
print("seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
print("seu primeiro nome tem {} letras".format(nome.find(' ')))
