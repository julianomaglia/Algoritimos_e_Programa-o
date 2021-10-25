from abc import ABCMeta, abstractmethod, abstractproperty

class Computador(metaclass=ABCMeta):

    @property
    def modelo(self):
        pass

    @modelo.setter
    @abstractmethod
    def modelo(self, modelo):
        pass

    @property
    def cor(self):
        pass

    @cor.setter
    @abstractmethod
    def cor(self, cor):
        pass

    @property
    def preco(self):
        pass

    @preco.setter
    @abstractmethod
    def preco(self, preco):
        pass

    def getInformacoes(self):
        return self.modelo, self.cor, self.preco

    @abstractmethod
    def cadastrar(self):
        pass


    def imprimir(self):
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Preço: ", self.preco)
