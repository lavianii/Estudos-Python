valorDaCasa = float(input('Qual o valor da casa: '))
salario = float(input('Seu salario: '))
anos = int(input('Em quantos anos você vai pagar: '))

parcela = valorDaCasa // (anos * 12)
prestaçao = salario * 30/100


if parcela >= prestaçao:
    print('Você NÃO pode financiar esta casa, pois 30% do seu salario é R${:.2f}'.format(prestaçao))
    print('Parcela: R${:.2f}'.format(parcela))
else:
    print('Voce PODE financiar esta casa, sua parcela ficará R${:.2f}'.format(parcela))