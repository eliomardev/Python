# Calcula IMC
import math

print("\n******** Calcula Índice de Massa Corpórea *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Qual o valor da sua altura (H) em metros? '))
n2=float(input('Qual o valor da massa (M) em quilogramas? '))
imc=(n2/n1**2)

print ('a sua altura e {} e a sua massa e {} e o IMC é {}'. format(n1, n2, imc))
