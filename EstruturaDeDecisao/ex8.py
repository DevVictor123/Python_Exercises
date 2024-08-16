#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
produto1 = float(input("Digite primeiro produto: "))
produto2 = float(input("Digite segundo produto: "))
produto3 = float(input("Digite terceiro produto: "))


if produto1 < produto2 and produto1 < produto3:
    menor = produto1

elif produto2 < produto3:
    menor = produto2
    
else:
    menor = produto3

print(f"Produto mais barato: {menor}")