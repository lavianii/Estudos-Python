import math
c = '='
co = float(input('Digite o valor do Cateto Oposto: '))
print('A raiz quadra de {} é {}'.format(co, math.pow(co, 2)))
ca = float(input('Digite o valor do Cateto Adjacente: '))
print('A raiz quadra de {} é {}'.format(ca, math.pow(ca, 2)))
h = (math.pow(ca, 2)) + (math.pow(co, 2))
print (c * 50)
print('A soma dos catetos são {}'.format(h))
print('O valor da hipotenuza é {:.2f}'.format(math.sqrt(h)))
print('============== Segunda forma ================')
# Segunda forma
co2 = float(input('Digite o calor do Cateto Oposto: '))
ca2 = float(input('Digite o valor do Cateto Adjacente: '))
h2 = math.hypot(co2, ca2)
print('A hipotenuza é {:.2f}'.format(h2))

