from Furadeira import Furadeira
from Lixadeira import Lixadeira

#Paranmetros de Entrada
Furadeira = Furadeira("Bosh","110V",80,1000)

Lixadeira = Lixadeira("Makita","220V",100,2000)


print("\nFuradeira Cadastrada: ")
Furadeira.cadastrar()

print("\nListar Furadeira: ")
Furadeira.imprimir()

print("\nPrint Get Furadeira: ",Furadeira.getInformacoes())

print("\nLixadeira Cadastrada: ")
Lixadeira.cadastrar()

print("\nListar Lixadeira: ")
Lixadeira.imprimir()

print("\nPrint Get Lixadeira: ",Lixadeira.getInformacoes())
