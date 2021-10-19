from abc import ABCMeta, abstractmethod, abstractproperty

class Ferramenta(metaclass=ABCMeta):

    @property
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass

    @property
    def tensao(self):
        pass

    @tensao.setter
    @abstractmethod
    def tensao(self, tensao):
        pass

    @property
    def preco(self):
        pass

    @preco.setter
    @abstractmethod
    def preco(self, preco):
        pass

    def getInformacoes(self):
        return self.nome, self.tensao, self.preco

    @abstractmethod
    def cadastrar(self):
        pass


    def imprimir(self):
        print("Nome: ", self.nome)
        print("Tensao: ", self.tensao)
        print("Preço: ", self.preco)
