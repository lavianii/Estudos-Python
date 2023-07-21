from random import choice
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1, n2, n3, n4,]
sorteado = choice(lista)
print(sorteado)
print ('===== Segundo modo =====')

c = '='
alunos = 'ALUNO 1', 'ALUNO 2', 'ALUNO 3', 'ALUNO 4'
nome = choice(alunos)
print (c * 40)
print(nome)



