class Cachorro:
    def __init__(self, nome, idade, raca, comida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.energia = 100
        self.acordado = False
        self.feliz = False
    
    def comer(self):
        if self.acordado:
            if self.comida > 0:
                self.comida -= 1
                print(f"{self.nome} comeu tudinho!")
            else:
                print(f"{self.nome} não tem mais comida!")
        else:
            print(f"{self.nome} está dormindo e não pode comer...") 
    
    def dormir(self):
        self.acordado = False
        self.energia = 100
        print(f"{self.nome} está dormindo!") 
        print(f"{self.nome} recuperou as energias...")
        
    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado!")
    
    def latir(self):
        if self.acordado:
            print(f"{self.nome} latiu: AU AU!!")
        else:
            print(f"{self.nome} está dormindo e não pode latir!")
    
    def brincar(self):
        if self.acordado:
            if self.energia >= 20:
                self.energia -= 20
                self.feliz = True
                print(f"{self.nome} está brincando feliz!")
            else:
                print(f"{self.nome} está cansadinho e não pode brincar agora!")
        else:
            print(f"{self.nome} está dormindo e não pode brincar!")
    
    def ignorar(self):
        if self.acordado:
            self.feliz = False
            print(f"{self.nome} foi ignorado e está muito tristitinho! Reveja suas prioridades...")
        else:
            print(f"{self.nome} está dormindo e não tente ignorar seu cachorro enquanto ele está dormindo, seu sem coração!")
    

cachorro1 = Cachorro("Bandit", 6, "Buldogue Francês", 1)
cachorro2 = Cachorro("Caramelo", 4, "Vira-lata Caramelo", 2)

cachorro1.acordar()
cachorro1.brincar()
cachorro1.latir()
cachorro1.comer()
cachorro1.dormir()
cachorro1.ignorar()

cachorro2.acordar()
cachorro2.brincar()
cachorro2.latir()
cachorro2.comer()
cachorro2.dormir()
cachorro2.ignorar()    