from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nomePJ=None, fonePJ=None,cnpjPJ=None):
        super().__init__(nomePJ, fonePJ)
        self.cnpj = cnpjPJ

    def imprimir(self):
        print("Razão Social: ", self.nome)
        print("Telefone: ", self.fone)  
        print("CNPJ: ", self.cnpj)       