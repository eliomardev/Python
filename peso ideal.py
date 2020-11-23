sexo = input('Digite seu sexo: (1)Para homem (2)Para mulher: ')

if sexo == 1:
    aH = input('Digite sua altura: ')
    vH = 72.7 * aH
    rH = vH - 58
    print 'Seu peso ideal é ',rH,'quilos'
elif sexo == 2:
    aM = input('Digite sua altura: ')
    vM = 62.1 * aM
    rM = vM - 44.7
    print 'Seu peso ideal é ',rM,'quilos'

# Calcula Tempo no Laboratorio
import math

print("\n******** Calcula Tempo no Laboratorio *******") #irá imprimir na tela a mensagem de boas vindas

n1=float(input('Informe o tempo do laboratorio em segundos? '))

horas = n1 // 3600
segundos_rest = n1 % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print ('{} horas, {} minutos, e {} segundos'. format(horas, minutos, segundos_rest))