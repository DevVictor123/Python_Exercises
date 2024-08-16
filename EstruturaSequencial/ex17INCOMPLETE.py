#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: comprar apenas latas de 18 litros; comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
from math import ceil

#TODO: get user input
metros = int(input("Digite o tamanho da area a ser pintada (em metros): "))

qtd_litros_tinta = metros // 6

qtd_latas = ceil(qtd_litros_tinta / 18)
preco_latas = qtd_latas * 80.00

qtd_galoes = ceil(qtd_litros_tinta / 3.6)
preco_galoes = qtd_galoes * 25.00



print("--------LATAS----------")
print(f"Quantidade de latas: {qtd_latas}")
print(f"Valor a pagar: {preco_latas}")

print("--------GALOES----------")
print(f"Quantidade de galoes: {qtd_galoes}")
print(f"Valor a pagar: {preco_galoes}")

print("--------LATAS E GALOES----------")













#TODO: 
