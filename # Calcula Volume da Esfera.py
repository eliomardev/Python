# Calcula Volume da Esfera
import math

print("\n******** Calcula Volume da Esfera *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Qual o raio da esfera? '))

ve=(4 * math.pi*(n1**3)/3)

print('O raio da esfera e {} e o Volume da Esfera é {}'. format(n1, ve))
