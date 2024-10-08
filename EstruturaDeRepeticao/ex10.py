#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1+1, num2):
    print(i)