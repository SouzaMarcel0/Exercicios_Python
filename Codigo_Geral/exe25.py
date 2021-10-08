
print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')

# Objetivo calcular a area de um triangulo retangulo

from math import hypot

co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))

hi = hypot(co, ca)

print('A hipotenusa do triangulo é: {:.2f}' .format(hi))
