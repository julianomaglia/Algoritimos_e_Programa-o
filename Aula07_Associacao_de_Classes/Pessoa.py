from Cidade import Cidade

class Pessoa:

        def __init__(self, id, nome, municipio: Cidade):
            self.id = id
            self.nome = nome
            self.municipio = municipio
    
        def imprimir(self):
            print("Pessoa ", self.id, " - ", self.nome)
            print(" mora em: ", self.municipio.nome)
            
