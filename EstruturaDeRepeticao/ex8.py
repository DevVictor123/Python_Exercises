#Faça um programa que leia 5 números e informe a soma e a média dos números.
numeros = []

for i in range(1, 6):
    num = int(input("Digite um numero: "))
    numeros.append(num)

soma = sum(numeros)
media = soma / len(numeros)

print(f"Soma: {soma}")
print(f"Media: {media:.2f}")