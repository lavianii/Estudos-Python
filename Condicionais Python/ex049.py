tabuada = int(input('Digite qual tabuada deseja multiplicar: '))
for t in range(0,11):
    print('{} X  {} = {}'.format(tabuada, t, tabuada*t))

## Usuário define até onde quer multiplicar
tabu = int(input('Digite a tabuada: '))
final = int(input('Digite até onde quer multiplicar: '))
for i in range(0,final+1):
    print('{} X {} = {}'.format(tabu, i, tabu*i))
