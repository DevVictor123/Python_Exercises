#Classe Quadrado: Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
    
    def mudarValor(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho
        print(f"valor lado alterado {self.tamanho_lado}")
    
    def valorLado(self):
        print(f"Valor lado: {self.tamanho_lado}")
    
    def calculcarArea(self):
        print(f"Area: {self.tamanho_lado * self.tamanho_lado}")
    
    def imprimeQuadrado(self):
        for i in range(self.tamanho_lado):
            print("*" * self.tamanho_lado)
        

quadrado_1 = Quadrado(4)

quadrado_1.valorLado()

quadrado_1.mudarValor(6)

quadrado_1.calculcarArea()

quadrado_1.imprimeQuadrado()

