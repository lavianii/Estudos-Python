class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return  f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(10,11,2020)

d2 = Data(11,12,2023)

print(d1)
print(d2)   