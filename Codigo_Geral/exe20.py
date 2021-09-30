
print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')



valor = float(input('Quanto dinheiro você quer converter Digite o valor em R$ '))

"""
valor = valor.__contains__(',')
if contains.valor == ',':
    valor = valor.replace (',', '.')
else:
    valor
    """

cotacao_atual_dollar = 3.40

calculo = valor / cotacao_atual_dollar

print(f'O seu dinheiro em R$ {valor} equivale a $ {calculo:.7} dollares')