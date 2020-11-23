# Folha de Pagamento
import math

print("\n******** Folha de Pagamento *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Informe o valor de sua hora de trabalho '))
n2=float(input('Informe a quantidade de horas trabalhadas '))
n3=float(input('Informe o numero de dependentes '))

sb=(n1*n2) #Calulo do Salario Bruto
inss=(sb*0.08) #Calculo do INSS
bene=(850+(sb*0.01))#Calculo do Beneficios valor de 850, mais 1% do salario bruto, 0.01 ou 1/100
ps=(sb*0.02)+((sb*0.01)*n3) #Calculo do Plano de Saude, 2% sobre o salario bruto, mais 1% do salario bruto sobre cada dependente
sl=sb-(inss+ps) #Calculo do salario liquido, o salario liquido menos os descontos, inss e plano de saude

print ('o valor da hora e {} a quantidade de horas trabalhadas e {} e o salario bruto {}'. format(n1, n2, sb))

print ('o valor do inss e {} o valor dos Beneficios sao {} e o Plano de Saude {}'. format(inss, bene, ps))

print ('o valor do salario liquido e {}'. format(sl))