class Funcionario:
    def _init_(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario
    
    def exibir_dados(self):
      print(f"nome: {self.__nome}")
      print(f"cpf: {self.__cpf}")
      print(f"salario: {self.__salario}")

class Gerente(Funcionario):
    def _init_(self, nome, cpf, salario, bonus):
        super()._init_(nome, cpf, salario)
        self.__bonus = bonus

    def exibir_dados(self):
        super().exibir_dados()
        print(f"bonus: {self.__bonus}")
        print(f"salario final: {self.get_salario() + self.__bonus}")

class Operacional(Funcionario):
    def _init_(self, nome, cpf, salario, turno):
        super()._init_(nome, cpf, salario)
        self.__turno = turno

    def exibir_dados(self):
        super().exibir_dados()
        print(f"turno: {self.__turno}")

funcionario1 = Gerente("Nana", 123456789, 1500.00, 2000.00)
funcionario1.exibir_dados()
funcionario2 = Operacional ("Carlos", 12345678, 1600.00, "Matutino")
funcionario2.exibir_dados()
