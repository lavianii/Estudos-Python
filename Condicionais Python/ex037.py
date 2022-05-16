
numero = int(input('Digite um numero para converter: '))
escolha = int(input('''
1 Para coverter Binário
2 Para converter Hexadecimal
3 Para converter Octal

Escolha qual modo de conversão:

'''))

if escolha == 1:
    print('{} convertido é {}'.format(numero,bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido é {}'.format(numero,hex(numero)[2:]))
elif escolha == 3:
    print('{} convertido é {}'.format(numero,oct(numero)[2:]))
else:
    print('Não existe essa opção')