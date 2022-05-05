salario = float(input('Qual seu salario: '))
if salario <= 1250:
    aumento = salario+(salario *15/100)
    print('Seu novo salário é: {:.2f}'.format(aumento))
else:
    aumento = salario+(salario *10/100)
    print('Seu novo salário é: {:.2f}'.format(aumento))

