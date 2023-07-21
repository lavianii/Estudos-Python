reta1 = float(input('1° reta: '))
reta2 = float(input('2° reta: '))
reta3 = float(input('3° reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É um triângulo')
    if reta1 == reta2 and reta2 == reta3:
        print('...Triângulo Equilátero')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3 :
        print('...Triângulo Isóceles')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('...Triângulo Escaleno')
else:
    print('Não é triângulo')

