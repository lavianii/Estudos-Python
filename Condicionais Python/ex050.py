soma = 0
for i in range(1,7):
    n = int(input(f'{i}° valor: '))
    if n %2==0:
        soma+=n
print(f'A soma dos numero pares é {soma} ')
