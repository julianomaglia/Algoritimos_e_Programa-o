from Computador import Computador

class Notebook(Computador):
    
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        self._modelo = modelo
        self._cor = cor
        self._preco = preco
        self.__tempoDeBateria = tempoDeBateria
    
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def nome(self, modelo):
        self._modelo = modelo

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def tensao(self, cor):
        self._cor = cor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    def cadastrar(self):
        super().imprimir()
        print("Tempo de Bateria é: ", self.__tempoDeBateria)      

    def getInformacoes(self):
        if  self.preco <= 7000:
            self.ta_Barato = "SIM"
            return print("Modelo:",self.modelo, "  Cor:",self.cor, "  Preço:",self.preco, "  Fonte:",self.__tempoDeBateria, "  Ta Barato?",self.ta_Barato)
             
        else: 
            self.ta_Barato = "Não"
            return print("Modelo:",self.modelo, "  Cor:",self.cor, "  Preço:",self.preco, "  Fonte:",self.self.__tempoDeBateria, "  Ta Barato?",self.ta_Barato)

