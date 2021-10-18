from Veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, modelo, ano, cilindradas):
        self._modelo = modelo
        self._ano = ano
        self._cilindradas = cilindradas

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        self._ano = valor

    @property
    def cilindradas(self):
        return self._cilindradas
    
    @cilindradas.setter
    def cilindradas(self, valor):
        self._cilindradas = valor

    def imprimir(self):
        print("Motocicleta: ")
        super().imprimir()

    def imprimirEspecifico(self):
        super().imprimir()
        print("Cilindradas: ", self.cilindradas)    