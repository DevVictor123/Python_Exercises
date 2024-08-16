#Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input("Digite primeiro numero: "))
num2 = int(input("Digite segundo numero: "))
num3 = int(input("Digite terceiro numero: "))

if num1 < num2:
    aux = num1
    num1 = num2
    num2 = aux

if num2 < num3:
    aux = num2
    num2 = num3
    num3 = aux

if num1 < num2:
    aux = num1
    num1 = num2
    num2 = aux

print(f"Ordem decrescente: {num1}, {num2}, {num3}")