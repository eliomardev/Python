# Calcula perimetro de um retângulo
import math

print("\n******** Calcula perimetro de um retângulo *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Qual o valor da base (L)? '))
n2=float(input('Qual o valor da altura (H)? '))
p=(2*n1)+(2*n2)
pol=p*0.393701
j=p*0.0109361

print ('os lados são {} e {} e o do perimetro é {} centimetros'. format(n1, n2, p))
print ('o perimetro em  polegas e {} e em jardas é {}'. format(pol, j))
