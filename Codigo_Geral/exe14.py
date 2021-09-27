

#Funcao lambda para ordernar em ordem crescente strig com inteiro, usando a posição inicial do INT para pedir a ordenação.

print ('**' * 18)
print ('**** Bem Vindo ao Meu Programa ****\n')


alunos = ['ALUNO_99', 'ALUNO_987', 'ALUNO_01', 'ALUNO_03', 'ALUNO_07', 'ALUNO_34']


print(sorted (alunos, key=lambda x: int(x[6:])))

