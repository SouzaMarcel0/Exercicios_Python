

print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')

def fibonacci (numero):
    if numero <= 1:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

x = int(input("digite um número de posição de seu fibonacci e descubra seu valor  "))
res = fibonacci(x - 1)

print(f"O fibonacci de {x} é {res}")