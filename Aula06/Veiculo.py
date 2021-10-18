from abc import ABCMeta, abstractmethod, abstractproperty

class Veiculo(metaclass=ABCMeta):

    @property
    def modelo(self):
        pass
    
    @modelo.setter
    @abstractmethod
    def modelo(self, valor):
        pass
    
    @property
    def ano(self):
        pass

    @ano.setter
    @abstractmethod
    def ano(self, valor):
        pass

    def imprimir(self):
        print("Todos Valores", self.modelo)
        print("Todos Ano", self.ano)


    @abstractmethod
    def imprimirEspecifico(self):
        pass