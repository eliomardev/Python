# Calcula Area do Cilindro
import math

print("\n******** Calcula Area do Cilindro *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Informe o valor do Raio do Cilindro? '))
n2=float(input('Informe o valor da altura do Cilindro? '))

base=(math.pi*n1**2)
lateral=(2*math.pi*n1*n2)
total=2*base+lateral
qlitros=total/3
qlata=qlitros/5
valor=qlata*50

print ('A area lateral do Cilindro e {} e a base e {}'. format(lateral, base))

print ('A area Total do Cilindro e {}'. format(total))

print ('A quantidade total de litros e {} e quantidade de latas e {}'. format(qlitros, qlata))

print ('O valor total para a pintura do cilindro e {}'. format(valor))


