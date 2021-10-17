from Produto import Produto

p1 = Produto()
p1.imprimir()

p1.preco = 19.9

print("Novo preco do produto: ", p1.nome)
print(p1.aumentarPreco(10))

print(p1.preco)
