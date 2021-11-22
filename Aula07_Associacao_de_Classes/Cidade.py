class Cidade:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.__populacao = 100
    
    def imprimir(self):
        print("Cidade ",self.id, " - ", self.nome)
        print("Total de moradores: ",self.__populacao)
    

        