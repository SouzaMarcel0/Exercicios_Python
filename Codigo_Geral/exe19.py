

print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')


lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reposta = int(input('Qual é o número?  '))

for numero in lista_de_numeros:
    print(f'{numero:2} x {reposta} = {reposta * numero}')
