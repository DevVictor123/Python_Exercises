#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input("Digite o valor da hora: "))
qtd_horas = int(input("Digite a quantidade de horas trabalhadas: "))

salario = valor_hora * qtd_horas

print(f"O seu salário no mês é: R${salario}")
