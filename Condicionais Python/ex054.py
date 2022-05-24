from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0
for i in range(1,8):
    nascimento = int(input(f'{i}° Pessoa, qual ano você nasceu? '))
    idade = anoAtual - nascimento 
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Tem {maior} maior de idade')
print(f'Tem {menor} menor de idade')