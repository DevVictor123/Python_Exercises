#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area = int(input("Digite o tamanho da area a ser pintada: "))
valor_tinta = 80.00

qtd_tinta = area // 3

qtd_latas = round(qtd_tinta / 18)

preco = qtd_latas * valor_tinta

print(f"quantidade de latas: {qtd_latas}")
print(f"Preco: {preco:.2f}")




