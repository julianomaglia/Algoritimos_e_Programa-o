from Cidade import Cidade
from Pessoa import Pessoa
from Fisica import Fisica

cid01 = Cidade(1, "Porto Alegre")
cid02 = Cidade(1, "Capão da Canoa")

p1 = Pessoa(1, "João", cid02)
p2 = Pessoa(2, "Maria", cid01)
p3 = Pessoa(3, "José", cid02)

cid01.imprimir()
print("----------------------------")
p1.imprimir()

print("-----------------------")

pf1 = Fisica(1, "J", cid01, "0000000")
pf1.imprimir()