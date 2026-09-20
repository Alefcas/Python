#Programa que conta a contagem regressiva de fogos de artificio
#Alef Castro
#20/09/2026
from time import sleep
seg = int(input("quantos segundos para estourar o fogo de artificio: "))
for cont in range(seg, 0, -1):
    print(cont)
    sleep(1)
print("BOOOOMM!!!")