#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
saque = int(input("Digite o valor do saque: "))


if saque < 10 or saque > 600:
    print("Valor invalido")

centena = 0
dezena = 0
unidade = 0

nota_100 = 0
nota_50 = 0
nota_10 = 0
nota_5 = 0
nota_1 = 0


centena = ((saque // 100) * 100) // 100
dezena = (((saque % 100) // 10) * 10)
unidade = saque % 10

if centena > 0:
    nota_100 = centena

while dezena >= 50:
    nota_50 += 1
    dezena -= 50

while dezena >= 10:
    nota_10 += 1
    dezena -= 10

while unidade >= 5:
    nota_5 += 1
    unidade -= 5

while unidade >= 1:
    nota_1 += 1
    unidade -= 1

if nota_100 != 0:
    print(f"notas de cem: {nota_100}")

if nota_50 != 0:
    print(f"notas de cinquenta:{nota_50}")

if nota_10 != 0:
    print(f"notas de dez: {nota_10}")

if nota_5 != 0:
    print(f"notas de cinco: {nota_5}")

if nota_1 != 0:
    print(f"notas de um: {nota_1}")



