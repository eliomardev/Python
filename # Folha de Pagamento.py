# Folha de Pagamento
import math

print("\n******** Folha de Pagamento *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Informe o valor de sua hora de trabalho '))
n2=float(input('Informe a quantidade de horas trabalhadas '))

sb=(n1*n2)
ir=(sb*0.11)
inss=(sb*0.08)
sind=(sb*0.05)
sl=sb-(ir+inss+sind)

print ('o valor da hora e {} a quantidade de horas trabalhadas e {} e o salario bruto {}'. format(n1, n2, sb))

print ('o valor do inss e {} o valor do imposto de renda {} e o sindicato {}'. format(inss, ir, sind))

print ('o valor do salario liquido e {}'. format(sl))