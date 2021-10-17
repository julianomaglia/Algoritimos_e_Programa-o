from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nomePF = None, fonePF = None, cpfPF = None):
        super().__init__(nomePF, fonePF)
        self.cpf = cpfPF

    def imprimir(self):
        super().imprimir() 
        print("CPF: ", self.cpf)   