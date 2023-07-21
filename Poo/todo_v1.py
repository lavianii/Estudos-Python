from datetime import datetime

class Tarefa:
    # construtor
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    # quando a tarefa for concluida faz com que o feito fica True
    def concluir(self):
        self.feito = True

    # retorna o tostring
    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else '')
    

def main():
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar Prato'))

    # verifica qual tarefa foi concluida
    for i,tarefa in enumerate(casa):
        if 'Lavar Prato' in casa[i].descricao:
           tarefa.concluir()

    # printa no console as tarefas
    for tarefa in casa:
        print(f'- {tarefa}')

main()