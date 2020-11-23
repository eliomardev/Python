# Calcula Tempo de Download
import math

print("\n******** Calcula Tempo de Download *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Informe o tamanho do arquivo em MegaBytes? '))
n2=float(input('Informe a velocidade do Link em Megabits/s? '))

t=(n1/(n2/8))

print ('O tempo de Download e igual a {}, segundos'. format(t))