#programa que leia três números e mostre qual é o maior e qual é o menor.
#Alef Castro
#02/09/2026
a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))
#Teste maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
#Teste menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print("Maior número: {} | Menor número {}". format(maior, menor))