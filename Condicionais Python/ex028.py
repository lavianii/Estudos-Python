from random import randint
from time import sleep
print('Pensando...')
sleep(3)
sorteador = randint(0, 5)

print('-' * 50)
print('Tente adivinhar qual numero estou sorteando')
tentativa = int(input('Qual numero foi sorteado de 0 a 5: '))
print('Verificando...')
sleep(3)

if sorteador == tentativa:
    print('Nosaa, que sorte, você acertou!!')
else:
    print('Haha, você erro tente outro dia')
if tentativa > 5:
    print('parece que você errou por muito, apenas vou até 5')