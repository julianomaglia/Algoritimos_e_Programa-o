from Desktop import Desktop
from Notebook import Notebook

#Paranmetros de Entrada
Desktop = Desktop("AMD","PRETO",8001,"700W")

Notebook = Notebook("Dell","Branco",7000,"7 Horas")


print("\nDesktop Cadastrado: ")
Desktop.cadastrar()

print("\nListar Desktop: ")
Desktop.imprimir()

print("\nPrint Get Desktop: ",Desktop.getInformacoes())

print("\nNotebook Cadastrado: ")
Notebook.cadastrar()

print("\nListar Notebook: ")
Notebook.imprimir()

print("\nPrint Get Notebook: ",Notebook.getInformacoes())
