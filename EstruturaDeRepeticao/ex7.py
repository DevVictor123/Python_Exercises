#Faça um programa que leia 5 números e informe o maior número.
numeros = []

for i in range(1, 6):
    num = int(input("Digite um numero: "))
    numeros.append(num)

numeros.sort(reverse=True)

maior = numeros[0]

print(f"Maior: {maior}")
