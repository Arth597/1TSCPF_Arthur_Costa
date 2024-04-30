# Crie um algoritmo que simule um temporizador. Peça os minutos e imprima um relógio de
# minutos e segundos. Utilize o FOR – um for dentro do outro. Repita o exerício usando o WHILE

from time import sleep

x = int(input('Digite os minutos para o temporizador:'))

for i in range(x):
     total =  i*60
     for segundos in range(total, reversed=True):

          print(segundos - 1)





