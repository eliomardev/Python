# Calculadora em Python

print("\n******** Calculadora Python *******") #irá imprimir na tela a mensagem de boas vindas ******** Calculadora Python *******

#def é uma palavra reservada (vimos isso durante nosso aprendizado) para representar uma função
def soma(x, y): #estamos definindo a função de soma. Onde esperamos duas entradas (ou duas variáveis - já vimos o conceito de variável)
	return x + y

def subtracao(x, y): #estamos definindo a função de de subtração.
	return x - y

def multiplicacao(x, y): #estamos definindo a função de multiplicação.
	return x * y

def divisao(x, y): #estamos definindo a função de divisão.
	return x / y

print("\nSelecione a operação desejada: \n") #imprimindo na tela uma mensagem. vimos isso durante a aprendizagem
print(" 1 -> Soma")
print(" 2 -> Subtração")
print(" 3 -> Multiplicação")
print(" 4 -> Divisão")

escolha = input("\nDigite sua opção (1/2/3/4): ") 
"""estamos aqui "coletando" o número da opção escolhida e atribuindo a variável "escolha".
vimos atribuição de valores a variáveis durante a aprendizagem"""

num1 = int(input("\nDigite o primeiro número: ")) 
"""estamos aqui coletando um valor, convertendo para o tipo "int" (inteiro) e atribuindo a variável num1.
a variável "num1" servirá de entrada para a variável "x" de cada função acima (soma, subtração, multiplicação e divisão)"""
num2 = int(input("\nDigite o segundo número: ")) 
"""estamos aqui coletando um valor, convertendo para o tipo "int" (inteiro) e atribuindo a variável num2
a variável "num2" servirá de entrada para a variável "y" de cada função acima (soma, subtração, multiplicação e divisão)"""

#bom. Aqui irá acontecer a "mágica". Temos uma cadeia de condicionais - Veremos logo logo nos nossos aprendizados. Portanto, detalheremos  melhor este trecho em uma nova oportunidade
if escolha == '1':
	print("\n")
	print(num1, "+", num2, "=", soma(num1, num2))
	print("\n")

elif escolha == '2':
	print("\n")
	print(num1, "-", num2, "=", subtracao(num1, num2))
	print("\n")

elif escolha == '3':
	print("\n")
	print(num1, "*", num2, "=", multiplicacao(num1, num2))
	print("\n")

elif escolha == '4':
	print("\n")
	print(num1, "/", num2, "=", divisao(num1, num2))
	print("\n")

else:
	print("\nOpção Inválida!")

"""bom. um programa simpels de calculadora, que envolve atribuições de variáveis, funções e condicionais. Pois bem, aproveite para
pesquisar os trechos do nosso código e breve voltaremos nele para melhorar. Muito Obrigado!"""