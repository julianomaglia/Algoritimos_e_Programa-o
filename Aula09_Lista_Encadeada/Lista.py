from No import No

class Lista:

# Metodo para Instanciar a Lista
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
#************************************

# Metodo para Adcionar na Lista
    
    def adicionar(self, valor):
        no = No(valor)
        if self.inicio: # Verifica se esta None ou Com valor - Caso seja None Vai para o ELSE
            aux = self.inicio #AUX recebe Inicio

            while (aux.proximo): 
                aux = aux.proximo
            
            aux.proximo = no
        
        else:
            self.inicio = no
        
        self.tamanho += 1
        
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print("Alista esta Vazia!")
        
        else:
            aux = self.inicio
            
            while(aux):

                print(aux.dado)
                aux = aux.proximo

            print("Tamanho da Lista", self.tamanho)
            print("------------------------------------")    

# Metodo para Excluir de dentro da Lista
    def excluir(self, valor):
        #Tratamento para Lista de Tamnho 1
        if self.tamanho == 0:
            print("A lista esta Vazia")
        
        elif self.tamanho == 1:
            if self.inicio.dado == valor:
                self.inicio = None
                self.tamanho = 0
            else:
                print("Valor não encontrado")
        #Tratamento para mais de 1

        else:
            tamanhoAnterior = self.tamanho
            if self.inicio.dado == valor:
                    self.inicio = self.inicio.proximo
                    self.tamanho -= 1
            else:
                anterior = self.inicio 
                aux = self.inicio.proximo
                while( aux):
                    if aux.dado == valor:
                        anterior.proximo = aux.proximo
                        self.tamanho -= 1
                    else:
                        anterior = aux
                    aux = aux.proximo

            if tamanhoAnterior == self.tamanho:
                print("Valor não encontrado")
        
        self.imprimir()
            