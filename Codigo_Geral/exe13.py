

print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')

preco = [34, 678, 640, 450, 100, 240]

impostos = list(map(lambda x: x * 0.3, preco))

print(f' 30% de {preco} é respectivamente : {impostos}\n')

