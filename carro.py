class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 0
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            print(f"O carro de modelo {self.modelo} ligou!")
        else:
            print(f"O carro de modelo {self.modelo} está sem combustível.")

    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
            print(f"O carro {self.modelo} foi desligado!")
        else:
            print(f"Esse {self.modelo} está em movimento, não pode desligar.")

    def acelerar(self):
        if self.ligado:
            if self.combustivel >= 5:
                self.velocidade += 10
                self.combustivel -= 5
                print(f"Seu {self.modelo} está a {self.velocidade} km/h.")
            else:
                print(f"O {self.modelo} não tem combustível suficiente para acelerar.")
        else:
            print(f"O {self.modelo} está desligado e não pode acelerar.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"O {self.modelo} freou, está {self.velocidade} km/h.")
        else:
            print(f"Esse {self.modelo} já está parado.")

    def abastecer(self, quantidade):
        if self.combustivel + quantidade <= 100:
            self.combustivel += quantidade
            print(f"Seu carro {self.modelo} foi abastecido, o combustível está agora em: {self.combustivel}.")
        else:
            print(f"O tanque está acima do limite de combustível.")

    def buzinar(self):
        print(f"{self.modelo} está buzinando: Beep Beep!")

    def status(self):
        estado = "ligado" if self.ligado else "desligado"
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, "
              f"Combustível: {self.combustivel}, Estado: {estado}, Velocidade: {self.velocidade} km/h.")

# Exemplo de uso
carro1 = Carro("Fusca", 1970, "azul")
carro1.abastecer(50)
carro1.ligar()
carro1.status()
carro1.acelerar()
carro1.buzinar()
carro1.frear()
carro1.desligar()