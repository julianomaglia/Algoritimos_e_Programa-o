class Conta:

        def __init__(self):

            self.__saldo = 0.0



        def __descontarTarifa(self):

                self.__saldo -= 1.99



        def depositar(self, valor):

                if valor > 0:

                        self.__saldo += valor

                        self.__descontarTarifa()

                        print("Valor depositado")

                else:

                        print("Valor não permitido")



        def sacar(self, valor):

                if valor > 0:

                        self.__saldo -= valor

                        self.__descontarTarifa()

                        print("Saque realizado")

                else:

                        print("Valor não permitido")



#        def getSaldo(self):

#               return self.__saldo



#        def setSaldo(self, valor):

#                admin = True

#                if admin == True :

#                        self.__saldo = valor

#                else:

#                        print("Acão permitida apenas para o Admin")

        @property
        def saldo(self):
            return self.__saldo

        @saldo.setter
        def saldo(self, valor):
            admin = True
            if admin:
                self.__saldo = valor

            else:
                print("Ação não permitida")
