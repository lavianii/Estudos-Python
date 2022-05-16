n1 = int(input('Digite 1° numero: '))
n2 = int(input('Digite 2° numero: '))

if n1 > n2:
    print('O numero {} é o maior'.format(n1))
elif n2 > n1:
    print('O numero {} é o maior'.format(n2))
elif n1 == n2:
    print('Os numeros {} e {} são iguais'.format(n1, n2))