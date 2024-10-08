#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
num = []

for i in range(0, 5):
    numero = int(input("digite um numero inteiro: "))
    num.append(numero)

print(f"Numeros digitados: {num}")