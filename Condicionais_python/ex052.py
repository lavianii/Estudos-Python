primo = int(input('Digite um numero: '))
divisor = 0
for i in range(1, primo+1):
    if primo % i == 0:
        divisor += 1
if divisor == 2:
    print('Primo')
else:
    print('Não primo')
    
        
