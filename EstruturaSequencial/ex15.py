#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:salário bruto.quanto pagou ao INSS.; quanto pagou ao sindicato.; o salário líquido.; calcule os descontos e o salário líquido, conforme a tabela abaixo
#input do usuario
valor_hora = float(input("Digite o valor da hora: "))
qtd_horas = int(input("Digite a quantidade de horas trabalhadas: "))

#calcula o salario mensal
salario = valor_hora * qtd_horas

#calcula os descontos de imposto
imposto_renda = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
descontos = inss + sindicato

#calcula salario liquido
salario_liquido = salario - descontos

print(f"Salario bruto: R${salario:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"Sindicato: R${sindicato:.2f}")
print(f"Salario liquido R${salario_liquido:.2f}")