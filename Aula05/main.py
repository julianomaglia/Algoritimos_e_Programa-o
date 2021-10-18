from Conta import Conta

c1 = Conta()

c1.depositar(100)

c1.sacar(50)

#print("Saldo: ", c1.getSaldo())

#c1.__saldo = 80

#print (c1.__saldo)

#c1.depositar(10)
#print(c1.__saldo)

#print("Saldo do objeto: ", c1.getSaldo())

print("Saldo: ", c1.saldo)
c1.depositar(50)
print("saldo final ", c1.saldo)