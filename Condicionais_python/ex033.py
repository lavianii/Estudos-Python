n1 =int(input('Digite 1° valor:')) 
n2 =int(input('Digite 2° valor:')) 
n3 =int(input('Digite 3° valor:')) 

#verifica qual o maior
if n1 > n2 < n1 > n3:
    print('Maior valor é: {}'.format(n1))
elif n2 > n1 < n2 > n3:
    print('Maior valor é: {}'.format(n2))
elif n3 > n1 < n3 > n2:
    print('Maior valor é: {}'.format(n3))
#verifica qual é o menor
if n1 < n2 > n1 < n3:
    print('Menor valor é: {}'.format(n1))
elif n2 < n1 > n2 < n3:
    print('Menor valor é: {}'.format(n2))
elif n3 < n1 > n3 < n2:
    print('Menor valor é: {}'.format(n3))
     
 