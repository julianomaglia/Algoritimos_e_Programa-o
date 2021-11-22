from Computador import Computador

class Desktop(Computador):
    
    def __init__(self, modelo, cor, preco, potencia_fonte):
        self._modelo = modelo
        self._cor = cor
        self._preco = preco
        self._potencia_fonte = potencia_fonte
   
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
    def cor(self, cor):
        self._cor = cor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    def cadastrar(self):
        super().imprimir()
        print("Potencia da Fonte é: ", self._potencia_fonte)   

    def getInformacoes(self):
        if  self.preco <= 8000:
            self.ta_Barato = "SIM"
            return print("Modelo:",self.modelo, "  Cor:",self.cor, "  Preço:",self.preco, "  Fonte:",self._potencia_fonte, "  Ta Barato?",self.ta_Barato)
             
        else: 
            self.ta_Barato = "Não"
            return print("Modelo:",self.modelo, "  Cor:",self.cor, "  Preço:",self.preco, "  Fonte:",self._potencia_fonte, "  Ta Barato?",self.ta_Barato)

       