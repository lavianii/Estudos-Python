nome = str(input('Digite seu nome completo: ')).strip()

print('Todas as letras maiúsculas: {}'.format(nome.upper()))
print('Todas as letras minúsculas: {}'.format(nome.lower()))
espaco = nome.count('')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
dividido=nome.split()# Separa o indice [Jonas] [Soares] [Laviani]
#                                          0       1         2
print('Seu primeiro nome tem {} letras'.format(len(dividido[0]))) 
# Irá contar apenas o primeiro indice [Jonas]
#                                      12345  RESULTADO SEU PRIMEIRO NOME CONTÉM 5 LETRAS 

