distancia = float(input('Qual a distância de sua viagem: '))

if distancia <= 200:
    passagem = distancia * 0.50
    print('Sua passagem ficou: R${:.2f}'.format(passagem))
if distancia > 200:
    passagem = distancia * 0.45
    print('Sua passagem ficou: R${:.2f}'.format(passagem))

