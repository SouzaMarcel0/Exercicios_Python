'''
Faça um programa que leia 5 números e informe o maior número.
'''

print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****')

n_1 = float(input('Digite um número:   '))
n_2 = float(input('Digite um número:   '))
n_3 = float(input('Digite um número:   '))
n_4 = float(input('Digite um número:   '))
n_5 = float(input('Digite um número:   '))


if n_1 > n_2 > n_3 > n_4 > n_5 :
    print(n_1)
elif n_2> n_3 > n_4 > n_5 > n_1:
    print(n_2)
elif n_3 > n_4 > n_5 > n_2 > n_1:
    print(n3)
elif n4 > n_5 > n_1 > n_2 > n_1 :
    print(n_4)
elif n5 > n_1 > n_2 > n_3 > n_4 :
    print(n5)
else :
    print('todos são iguais')


