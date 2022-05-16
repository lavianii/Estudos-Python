
from datetime import date
anoAtual = date.today().year
anoDeNascimento = int(input('Digite o seu ano de nascimento: '))
idade = anoAtual - anoDeNascimento
print('Você tem {} anos'.format(idade))
if idade <= 18:
    aindaFalta = 18-idade
    print('Você ainda vai se alistar')
    print('Falta {} ano(s) para se alistar'.format(aindaFalta))
elif idade > 18:
    print('Você já deveria ter se alistar ')




