#Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

if num1 > num2:
    print(f"{num1} é maior")

elif num2 > num1:
    print(f"{num2} é maior")

else:
    print("Os números são iguais")