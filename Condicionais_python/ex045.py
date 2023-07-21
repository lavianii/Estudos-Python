import random
jogada=int(input('''Digite qual você quer jogar:

1 Pedra
2 Tesoura 
3 Papel
ESCOLHA SUA JOGADA: 

'''))
print('='*50)
print('        ----------- JO - KEN - PÔ !! --------')
print('='*50)
jogadapc=['Pedra','Papel','Tesoura']
sorteador = random.choice(jogadapc)
if jogada == 1:
    if sorteador == 'Papel':
        print('O computador VENCEU, escolheu Papel')
    elif sorteador == 'Pedra':
        print('Empatamos !!')
        print('Também foi escolhido Pedra')
    elif sorteador == 'Tesoura':
        print('Você GANHOU, teve sorte, foi escolhido Tesoura')
elif jogada == 2:
    if  sorteador == 'Pedra':
        print('O computador VENCEU, escolheu Pedra')
    elif sorteador == 'Tesoura':
        print('Empatamos !! ')
        print('Também foi escolhido Tesoura')
    elif sorteador == 'Papel':
        print('Você GANHOU, teve sorte, foi escolhido Papel')
elif jogada == 3:
    if  sorteador == 'Tesoura':
        print('O computador VENCEU, escolheu Tesoura')
    elif sorteador == 'Papel':
        print('Empatamos !!')
        print('Também foi escolhido Papel')
    elif sorteador == 'Pedra':
        print('Você GANHOU, teve sorte, foi escolhido Pedra')
else:
    print('Opção inválida')
