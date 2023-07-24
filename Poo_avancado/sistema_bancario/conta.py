from abc import ABC, abstractmethod

class Conta(ABC, Cliente):
    
    def __init__(self, numero, Cliente):
        self._numero = numero
        self._saldo = 0
        self._agencia = '01'
        self._cliente = Cliente

    def depositar(self, valor):
        if valor < 0:
            return False
        else:
            self._saldo += valor
            return True
  

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            return True
        else:
            return False
     
    @classmethod
    def nova_conta(cls,numero, Cliente):
        return cls(numero, Cliente)

    @property
    def saldo(self):
        return self._saldo
    
class ContaCorrente(Conta):

    def __init__(self, numero, Cliente):
        super().__init__(numero, Cliente)
        self._limite = 100
        self._limite_saques = 3
    
  
    def sacar(self, valor):
        if self._limite_saques == 0:
            print('Limite de saque atingido')
            return False
        else:
            self._limite_saques -= 1
            return super().sacar(valor)

    def __str__(self):
        return f'Numero da conta: {self._numero}\n' \
               f'Agencia: {self._agencia}\n' \
               f'Saldo: {self.saldo}\n' \
               f'Quanditade de saques: {self._limite_saques}'


