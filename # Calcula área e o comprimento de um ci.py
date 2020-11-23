# Calcula área e o comprimento de um círculo de Raio
import math

print("\n******** Calcula área e o comprimento de um círculo de Raio *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Qual o valor do Raio? '))

a=math.pi*(n1**2)
c=2*math.pi*n1

print ('O raio é {} a area do circulo: {} e o comprimento é {}'. format(n1, a, c))
