#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def descricao(self):
        print(f"cor: {self.cor}")
        print(f"circunferencia: {self.circunferencia}")
        print(f"material: {self.material}")
    
    def trocarCor(self):
        self.cor = input("Digite a nova cor: ")
    
    def mostrarCor(self):
        print(f"A cor da bola eh {self.cor}")

bola_1 = Bola('Azul', 30, 'couro sintetico')

bola_1.descricao()

bola_1.trocarCor()

bola_1.mostrarCor()