
"""
Código permite escalar ou aumentar as possibilidades de incluir os valores/argumentos da função def(), que originalmente
precisa ter definido o número de argumentos para ser usada.
Retorna uma TUPLA com números/valores/objetos definidos na função.
"""

print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')


def f (*args): 
    print(f'\nargs = {args}')
    for arg in args: 
        print(arg)


f ()
f (1)
f (2, 3)
f (3, 2, 1)
f ('Recife', 'Pernambuco')