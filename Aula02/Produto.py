class Produto:

    def __init__(self, qtd = 100): #Podemos passar um valor dfault para o paremtro caso não seja informado na incialização do metodo
        self.nome = input("Digite o nome do Produto: ")
        self.preco = 0
        self.quantidade = qtd

    def imprimir(self):
        print("Nome: ", self.nome)
        print("Preço: ", self.preco) 
        print("Quantidade: ", self.quantidade)     

    def aumentarPreco(self, percentual):
        self.preco += self.preco * percentual / 100
        return self.preco

