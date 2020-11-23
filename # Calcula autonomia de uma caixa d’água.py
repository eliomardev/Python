# Calcula autonomia de uma caixa d’água
import math

print("\n******** Calcular autonomia de uma caixa d’água *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Informe o valor do Raio do Cilindro? '))
n2=float(input('Informe o valor da altura do Cilindro? '))

base=(math.pi*n1**2)
lateral=(2*math.pi*n1*n2)
total=2*base+lateral
volume=(base*n2)*1000
consumo=volume/1350

print ('O volume em litros e {}'. format(volume))

print ('A automia da Caixa Dagua em horas e {}'. format(consumo))


