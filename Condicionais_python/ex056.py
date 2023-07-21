mediaIdade = 0 
maiorIdade = 0
nomeVelho = ''
qtdM = 0
for i in range(1,5):
    print(f'=-=-=-=-= {i}° PESSOA =-=-=-=-=')
    nome = str(input('Qual seu nome: ')).upper().strip()
    sexo = str(input('[M/F]: ')).upper().strip()
    idade = int(input('Qual sua idade: '))
    mediaIdade += idade
    if i == 1 and sexo == 'M':
        maiorIdade = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome
    if sexo == 'F' and idade < 20:
        qtdM = qtdM + 1
media = mediaIdade / 4
print(f'A media de idade do grupo e: {media}')
print(f'O homem mais velho é {nomeVelho} com a idade de {maiorIdade}')
print(f'Tem {qtdM} de mulheres menores de 20 anos')




