maior = 0
menor = 0
for i in range(1,6):
    peso = float(input(f'Peso da {i}° pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}Kg')
print(f'O menor peso é {menor}Kg')