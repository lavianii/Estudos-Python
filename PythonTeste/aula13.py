#PARA CONTAR DE 1 ATÉ 5
from re import S


for c in range(1,6):
    print(c)
print('FIM')
#PARA CONTAR DE 1 ATÉ 6
for c in range(1,7):
    print(c)
print('FIM')

#PARA CONTAR AO CONTRÁRIO
for c in range(6,0,-1):
    print(c)
print('FIM')

#PARA CONTAR PULANDO
for c in range(0,7,2):
    print(c)
print('FIM')

#PARA RECEBER DADOS DO TECLADO 
n = int(input('Digite um número: '))
for c in range(0,n):
    print(c)
print('FIM')

n = int(input('Digite um numero: '))
for c in range(0,n+1):
    print(c)
print('FIM')

i = int(input('Inicio: '))
f = int(input('FIM: '))
p = int(input('Pular: '))

for c in range(i,f+1,p):
    print(c)
print('FIM')

s=0
for c in range(0,3):
    n = int(input('Digite um valor: '))
    s = s + n
print('A soma desses valores é: {}'.format(s))
print('FIM')