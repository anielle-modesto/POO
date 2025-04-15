class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor de depósito inválido")

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Valor inválido")

# Teste
conta = ContaBancaria("Maria", 23000)
print(conta.get_saldo())
conta.set_saldo(-30000)
print(conta.get_saldo())
