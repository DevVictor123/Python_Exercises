#Altere o programa anterior para mostrar no final a soma dos números.
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

if num1 > num2:
    num1, num2 = num2, num1

soma = 0

for i in range(num1+1, num2):
    print(i)
    soma += i

print(f"soma: {soma}")
    
