#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
num = []

for i in range(0, 10):
    numero = float(input("digite um numero real: "))
    num.append(numero)
    
num.reverse()
print(f"Numeros na ordem inversa: {num}")