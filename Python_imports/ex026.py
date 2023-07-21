nome= str(input('Digite o algo: ')).lower().strip()
print('A quantidade de letra "a" nessa plavra é :{} '.format(nome.count('a')))
print('A posição da primeira vez que a letra "a" aparece é: {}'.format(nome.find('a')+1))
print('A posição da ultima vez que a letra "a" aparece é: {}'.format(nome.rfind('a')+1))