# Calcula autonomia do carro
import math

print("\n******** Calcula autonomia do carro *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Informe o valor do Raio do Tanque? '))
n2=float(input('Informe o valor da altura do Tanque? '))


volume=(math.pi*n1**2*n2)
autonomia=(volume*10)

print ('O volume em litros e {}'. format(volume))

print ('A autonomia do carro e {}'. format(autonomia))