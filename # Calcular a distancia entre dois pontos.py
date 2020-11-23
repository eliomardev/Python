# Calcular a distancia entre dois pontos
import math

print("\n******** Calcular a distancia entre dois pontos *******") #irá imprimir na tela a mensagem de boas vindas

x1=float(input('Informe o valor de x do ponto P? '))
y1=float(input('Informe o valor de y do ponto P? '))
x2=float(input('Informe o valor de x do ponto Q? '))
y2=float(input('Informe o valor de y do ponto Q? '))

p=((x2-x1)**2)
q=((y2-y1)**2)

d=(p+q)*0.5

print ('A distância entre dois pontos quaisquer do plano e {}'. format(d))

