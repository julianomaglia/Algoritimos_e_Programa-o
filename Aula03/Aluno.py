from PessoaFisica import PessoaFisica

class Aluno(PessoaFisica):
    
    def __init__(self, nomeA, foneA, cpfA, matriculaA):
        super().__init__(nomeA, foneA, cpfA)
        self.matricula = matriculaA
       
    def imprimir(self):
        super().imprimir()   
        print("Matricula: ",self.matricula)
