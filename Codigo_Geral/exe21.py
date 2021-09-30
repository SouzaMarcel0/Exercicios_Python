

print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****')

altura_parede = float(input('Qual a altura da sua parede?  '))
largura_parede = float(input('Qual a largura da sua parede?  '))

area_parede = largura_parede * altura_parede

redimento_tinta = 2/1

qtde_tinta_necessaria = area_parede / redimento_tinta

print(f'A área total da sua parede é {area_parede} m², você precisará de {qtde_tinta_necessaria:.3} litros para pintar')




