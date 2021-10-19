from Ferramenta import Ferramenta

class Furadeira(Ferramenta):
    
    def __init__(self, nome, tensao, preco, potencia):
        self._nome = nome
        self._tensao = tensao
        self._preco = preco
        self._potencia = potencia
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def tensao(self):
        return self._tensao

    @tensao.setter
    def tensao(self, tensao):
        self._tensao = tensao

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    def cadastrar(self):
        super().imprimir()
        print("Potencia é de: ", self._potencia)   

    def getInformacoes(self):
        return self.nome, self.tensao, self.preco, self._potencia     