from Produto import Produto
from datetime import date

class Perecivel(Produto):

    def __init__(self, nome = None, preco = 0.0, validade = date.today()):
        super().__init__(nome, 5.25)
        self.validade = validade
    
    def cadastrar(self):
        super().cadastrar() #Aproveitei a implementação da classe Produto
        print("Este produto tem validade até", self.validade,)
        #print("O produto", self.nome, " De Preço ", self.preco, " Com Validade ", self.validade, " Foi Cadastrado!") #neste trecho reimplementamos o metodo da classe produto dentro da classe Prerecivel

    def alterarPreco(self, percentual):    
        percentual *= 2
        super().alterarPreco(percentual)
