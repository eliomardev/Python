# Calcula Tempo no Laboratorio
import math

print("\n******** Calcula Tempo no Laboratorio *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Informe o tempo do laboratorio em segundos? '))

horas = n1 // 3600
segundos_rest = n1 % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print ('{} horas, {} minutos, e {} segundos'. format(horas, minutos, segundos_rest))
