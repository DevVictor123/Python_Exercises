#Faça um Programa que peça as 4 notas bimestrais e mostre a média
notas = []
soma = 0

for i in range(4):
    notas.append(float(input(f"nota {i+1}: ")))

media = sum(notas) / len(notas)

print(f"media = {media:.2f}")


