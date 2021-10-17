class Produto:

    def __init__(self, nome = None, preco = 0.0):
        self.nome = nome
        self.preco = preco

    def cadastrar(self):
        print("O Produto ",self.nome, "de preço ",self.preco, "Foi cadatsrado no banco!")

    def alterarPreco(self, percentual):
        self.preco += self.preco * percentual / 100