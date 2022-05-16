from datetime import date
anoAtual = date.today().year
anoNascimento = int(input('Digite ano de nascimento para saber sua categoria: '))
idade = anoAtual - anoNascimento
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade > 9 and idade > 14 and idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade > 9 and idade > 14 and idade > 19 and idade <= 20:
    print('Sua categoria é SÊNIOR')
elif idade > 9 and idade > 14 and idade > 19 and idade > 20 and idade >= 21:
    print('Sua categoria é MASTER')

    