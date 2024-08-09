#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:o produto do dobro do primeiro com metade do segundo .a soma do triplo do primeiro com o terceiro.o terceiro elevado ao cubo.
valor1 = int(input("Digite um numero inteiro: "))
valor2 = int(input("Digite outro numero inteiro: "))
valor3 = float(input("Digite um numero real: "))

operacao1 = (valor1 * 2) * (valor2 / 2)
operacao2 = (valor1 * 3) + valor3
operacao3 = valor3 ** 3

print(f"O produto do dobro do primeiro com metade do segundo: {operacao1}")
print(f"A soma do triplo do primeiro com o terceiro: {operacao2}")
print(f"O terceiro elevado ao cubo: {operacao3:.2f}")

