class Carro:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
    
    def exibir_placas(self):
        print(f'Placa {self.placa}')

c1 = Carro("Fusca", "ABC-1234", 1970)
c2 = Carro("Gol", "XYZ-5678", 2010)
c2.exibir_placas()
