#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []

for i in range(0, 4):
    nota = float(input(f"Digite a notas {i+1}: "))
    notas.append(nota)

media = sum(notas) / 4

print(f"Notas: {notas}")
print(f"Media: {media}")