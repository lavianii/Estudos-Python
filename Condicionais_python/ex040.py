nota1 = float(input('Digite 1° nota: '))
nota2 = float(input('Digite 2° nota: '))

media = (nota1 + nota2) / 2

print(media)
if media < 5.0:
    print('REPROVADO, sua nota foi: {:.2f}'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('RECUPERÇÃO, sua nota foi: {:.2f}'.format(media))
elif media >= 7.0:
    print('APROVADO, sua nota foi: {:.2f}'.format(media))

