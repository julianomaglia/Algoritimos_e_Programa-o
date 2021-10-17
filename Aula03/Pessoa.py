class Pessoa:
    def __init__(self, nomePessoa = None, fonePessoa = None ):
        self.nome = nomePessoa
        self.fone = fonePessoa

    def imprimir(self):
        print("Nome: ", self.nome)    
        print("Telefone: ", self.fone)

        