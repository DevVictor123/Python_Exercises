#Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int(input("Digite primeiro numero: "))
num2 = int(input("Digite segundo numero: "))
num3 = int(input("Digite terceiro numero: "))

maior = 0
menor = 0

if num1 > num2 and num1 > num3:
    maior = num1

elif num2 > num3:
    maior = num2
    
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1

elif num2 < num3:
    menor = num2
    
else:
    menor = num3

print(f"Maior: {maior}\nMenor: {menor}")