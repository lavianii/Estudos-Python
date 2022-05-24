frase= str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
contrario = ''
for letras in range(len(junto) -1, -1, -1):
    contrario =contrario + junto[letras]
print(f'Inverso de {junto} é {contrario}')
if contrario == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')