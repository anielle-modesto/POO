class Animal:
    def _init_(self, nome):
        self.nome = nome
        super()._init_(nome)
        self.raca = raca

    def fazer_som(self)
        print("O animal faz um som.")

class Cachorro(Animal):
    def_init_(self, raca):
        super()._init_(nome)
        self.raca = raca
        
    def fazer_som(self):
        print(f"{self.nome} diz: Au Au!)

class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} diz: Miau Miau!")

dog = Cachorro("Caramelo", "Vira-Lata Caramelo")
dog.fazer_som()

gato1 = Gato("Azure", "Gato Preto")
gato1.fazer_som()
