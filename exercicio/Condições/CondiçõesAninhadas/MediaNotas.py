#Programa que leia duas notas e calcula a media mostrando a mensagem:
#REPROVADO ou RECUPERAÇÃO ou APROVADO
#Alef Castro
#11/09/2026
print("="*20)
print("AVALIANDO ALUNO")
print("="*20)

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1+n2)/2
print("Média do Aluno: {}".format(media))
if media < 5.0:
    print("REPROVADO!")
elif media < 7.0:
    print("RECUPERAÇÃO!")
else:
    print("APROVADO")