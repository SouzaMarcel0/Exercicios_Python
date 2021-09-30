

print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')

def fatorial (numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero -1)

x = int(input("Digite um número para calcular seu fatorial  "))
res = fatorial(x)

print(f"O fatorial de {x} é {res}")