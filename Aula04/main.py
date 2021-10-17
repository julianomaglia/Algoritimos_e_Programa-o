from Produto import Produto
from Perecivel import Perecivel

p = Produto("Pepsi", 4.99)

pr = Perecivel("Iorgute", 6.49, "17/10/2021")
pr.cadastrar()
pr.alterarPreco(10)
print("novo preco", pr.preco)