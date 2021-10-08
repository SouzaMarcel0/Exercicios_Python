
# Pode se importar a biblioteca inteira MATH ou apenas um "METODO" da bibliote para se aplicar no número e gerar
#  a formatação desejada ou simplesmente usar a função nativa do python para atender a demenda pela formatação.

# Objetivo: Escrever um código que peça um número float e mostre qual a sua parte inteira.

import math

num = float(input('Digite um número: '))

print('O número digitado foi {} e a sua porção inteira é {}' .format(num, math.trunc(num)))

print('O numero digitado foi {} e a sua porção inteira é {}' .format(num, int(num)))