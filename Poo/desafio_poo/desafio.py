from datetime import datetime as dt

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def is_adulto(self):
        if self.idade >= 18:
            return True
        return False
        
    def __str__(self):
        if not self.is_adulto():
            return self.nome
        return f'{self.nome} ({self.idade} anos)'
    

class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(compra)


    def get_data_ultima_compra(self):
        return f'A ultima compra foi no dia "{self.compras[-1].data}"com o valor {self.compras[-1].valor},00'

    
    # def get_data_ultima_compra(self):
    #     if not self.compras:  # Verifica se a lista de compras está vazia
    #         print(f'O cliente {self.nome} ainda não fez nenhuma compra.')
    #     else:
    #         ultima_compra = self.compras[-1]
    #         data_ultima_compra = dt.now()
    #         print(f'A ultima compra de "{self.nome}" foi feita em {ultima_compra.data} no valor de R${ultima_compra.valor:.2f} e a data atual é {data_ultima_compra}')    
    
    def total_compras(self):
        return len(self.compras)
    

class Compra(Cliente):
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor
        

def main():
    juracy = Cliente('Juracy Filho', 44)
    leo = Vendedor('Leonardo Leitao', 36, 1000)
    compra1 = Compra(leo, dt.now(), 512)
    compra2 = Compra(leo, dt(2018, 6, 4), 256)
    juracy.registrar_compra(compra1)
    juracy.registrar_compra(compra2)
    
    print(f'Cliente: {juracy}')
    print(f'Vendedor: {leo}')
    print(f'Total: {juracy} teve {juracy.total_compras()} compras')
    print(juracy.get_data_ultima_compra())
 
  
if __name__ == '__main__':

    main()


