
print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')

import math

angulo = float(input('Digite o valor do ângulo: '))

seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))


print('O seno de {} é {:.2f}'.format(angulo, seno))
print('O Coseno de {} é {:.2f}'.format(angulo, coseno))
print('A Tangente de {} é {:.2f}'.format(angulo, tangente))

