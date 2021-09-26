#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
#em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
#de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
#litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a
#serem compradas e o preço total


print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')

qtde_litros_lata = 18.0
valor_lata = 80.00
cobertura = 3


area = float(input('Qual a area que sera pintada em Metros Quadrados?   '))

total_litros_necessario = (area / cobertura)
total_latas_necessaria = (total_litros_necessario / qtde_litros_lata)
total_a_pagar = (total_latas_necessaria * valor_lata)

print(f' \nVocé terá que pagar R$ {total_a_pagar}, pois usará {total_latas_necessaria} lata(s) de tinta(s)\n')




