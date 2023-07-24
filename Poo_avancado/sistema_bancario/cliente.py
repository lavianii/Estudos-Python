from conta import ContaCorrente


class Cliente:
    def __init__(self,endereco):
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self,numero, conta):
        return self._contas.append(ContaCorrente(numero, conta))
    
class PessoaFisica(Cliente):

    def __init__(self, endereco, nome, data_nascimento):
        super().__init__(endereco)
        self._nome = nome
        self._data_nasciemnto = data_nascimento

    def __str__(self) -> str:
        return f'Nome: {self._nome}'
    



