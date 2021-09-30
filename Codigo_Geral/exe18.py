

print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')


texto = input("Digite algo:  ")

print(f'O que foi digitado é: {type(texto)}')
print(f'O que foi digitado tem espaço: {texto.isspace()}')
print(f'O que foi digitado é um número: {texto.isnumeric()}')
print(f'O que foi digitado é alfabetico: {texto.isalpha()}')
print(f'O que foi digitado é caixa alta: {texto.isupper()}')
print(f'O que foi digitado tem a primeira letra Maiúscula: {texto.islower()}')
print(f'O que foi digitado é Capitalizada: {texto.istitle()}')

