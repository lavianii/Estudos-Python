pa = int(input('Digite o primeiro termo da P.A: '))
rz = int(input('Digite qual vai ser a razão da: '))
d = pa+(10-1)*rz
print('-='*20)
for i in range(pa,d,rz):
    print(i, end='-')
print('/')
print('-='*20)