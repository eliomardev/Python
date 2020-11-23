# Calcula Hipotenusa
import math

print("\n******** Calcula Hipotenusa *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Qual o valor do primeiro cateto? '))
n2=float(input('Qual o valor do segundo cateto? '))
h=math.sqrt(n1**2+n2**2)

print ('os catetos são {} e {} e a hipotenusa é {}'. format(n1, n2, h))
