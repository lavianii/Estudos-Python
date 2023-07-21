from random import shuffle
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1, n2, n3, n4,]
print('Ordem de apresentação:')
print(lista)

print ('===== Segundo modo =====')
c = '='
alunos =['ALUNO 1', 'ALUNO 2', 'ALUNO 3', 'ALUNO 4']
shuffle(alunos)
print('Ordem de apresentação:')
print (c * 50)
print(alunos)
print (c * 50)