#Faça um Programa que leia três números e mostre o maior deles.
num1 = int(input("Digite um numero A: "))
num2 = int(input("Digite um numero B: "))
num3 = int(input("Digite um numero C: "))

if num1 > num2 and num1 > num3:
    print(f"Maior: {num1}")

elif num2 > num3:
    print(f"Maior: {num2}")
    
else:
    print(f"Maior: {num3}")
