produto = float(input('Qual valor do produto: '))
pagamento = int(input('''Qual a forma de pagamento? 
1 Para Dinheiro
-------------------------------------
2 Para Cartão
-------------------------------------
3 Para Cartão parcelado em 2x
-------------------------------------
4 Para Cartão parcelado em 3x ou mais
-------------------------------------
DIGITE: '''))

if pagamento == 1:
    desconto = produto-(produto*10/100)
    print('Desconto de 10%, {:.2f}'.format(desconto))
elif pagamento == 2:
    desconto = produto-(produto*5/100)
    print('Desconto de 5%, {:.2f}'.format(desconto))
elif pagamento == 3:
    parcela = produto / 2
    print('Sua parcela ficou, {:.2f}'.format(parcela))
elif pagamento == 4:
    juros = produto +(produto*20/100)
    jurosparcelado = int(input('Quantas parcelas? '))
    parcela = juros / jurosparcelado
    print('Sua compra será parcelada em {}x, no valor de {}'.format(jurosparcelado, parcela))
    print('O valor do seu produto com juros de 20% {}'.format(juros))
else:
    print('Opção inválida')