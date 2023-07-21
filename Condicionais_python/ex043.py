from time import sleep
print('Para calcular seu IMC Preciso saber sua altura e peso')
sleep(1)
print('Abrindo a calculadora')
sleep(1.5)
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura**2) 

if imc < 18.5:
    print('Abaixo do peso, {:.1f}'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Ideal, {:.1f}'.format(imc)) 
elif imc >= 25 and imc <= 30:
    print('Sobrepeso, {:.1f}'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Obesidade, {:.1f}'.format(imc))
elif imc > 40:
    print('Obesidade mórbida, {:.1f}'.format(imc))