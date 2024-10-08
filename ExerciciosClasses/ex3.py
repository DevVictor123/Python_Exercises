#Classe Retangulo: Crie uma classe que modele um retangulo:
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

'''Claro, posso te ajudar a entender como abordar esse problema!

Para calcular a quantidade de pisos e rodapés necessários para cobrir um retângulo, você precisa seguir algumas etapas:

1. **Determine as Medidas do Retângulo:**
   - Você já deve ter o comprimento e a largura do retângulo (o chão que será coberto).

2. **Determine as Medidas dos Pisos e Rodapés:**
   - **Pisos:** Você precisa saber as dimensões de cada peça de piso (por exemplo, comprimento e largura de cada azulejo ou cerâmica).
   - **Rodapés:** Semelhante aos pisos, você deve saber as dimensões de cada peça de rodapé (como a altura e a largura de cada peça).

3. **Calcule a Área do Retângulo:**
   - Área do retângulo = comprimento × largura.

4. **Calcule a Área de Cada Piso e Rodapé:**
   - Área de cada piso = comprimento do piso × largura do piso.
   - Área de cada rodapé = comprimento do rodapé × largura do rodapé.

5. **Calcule o Número de Pisos Necessários:**
   - Número de pisos necessários = Área total do retângulo ÷ Área de cada piso.
   - Certifique-se de arredondar para cima, pois você não pode usar uma fração de um piso.

6. **Calcule o Número de Rodapés Necessários:**
   - Primeiro, calcule o perímetro do retângulo: Perímetro = 2 × (comprimento + largura).
   - Número de rodapés necessários = Perímetro ÷ Comprimento de cada rodapé.
   - Novamente, arredonde para cima se necessário.

### Exemplo:

Vamos supor que o comprimento do retângulo seja 5 metros e a largura seja 4 metros.

- **Área do retângulo:** 5 m × 4 m = 20 m²

Se cada piso tem dimensões de 0,5 m × 0,5 m:

- **Área de cada piso:** 0,5 m × 0,5 m = 0,25 m²
- **Número de pisos necessários:** 20 m² ÷ 0,25 m² = 80 pisos

Se o rodapé tem 2 m de comprimento e 0,1 m de largura:

- **Perímetro do retângulo:** 2 × (5 m + 4 m) = 18 m
- **Número de rodapés necessários:** 18 m ÷ 2 m = 9 rodapés

Lembre-se de sempre considerar que é bom comprar um pouco mais de material para cobrir possíveis quebras ou ajustes.

Espero que isso ajude a esclarecer como você pode calcular a quantidade necessária de pisos e rodapés!'''
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        
    def mudaValor(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura
    
    def retornaValores(self):
        print(f"comprimento: {self.comprimento}")
        print(f"largura: {self.largura}")

    def calculaArea(self):
        print(f"area: {self.comprimento * self.largura}")

comprimento = int(input("Digite o comprimento: "))
largura = int(input("Digite a largura: "))


retagulo_1 = Retangulo(comprimento, largura)

retagulo_1.retornaValores()

