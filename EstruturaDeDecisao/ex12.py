#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.Desconto do IR:Salário Bruto até 900 (inclusive) - isentoSalário Bruto até 1500 (inclusive) - desconto de 5% Salário Bruto até 2500 (inclusive) - desconto de 10% Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
valor_hora = float(input("Digite o valor da hora: "))
qtd_horas = int(input("Digite a quantidade de horas trabalhadas: "))

#calcula o salario mensal
salario_bruto = valor_hora * qtd_horas

if salario_bruto <= 900:
    imposto_renda = 0
    inss = salario_bruto * 0.1
    sindicato = salario_bruto * 0.03
    fgts = 0
    descontos = sindicato
    salario_liquido = salario_bruto - descontos

elif salario_bruto > 900 and salario_bruto <= 1500:
    imposto_renda = salario_bruto * 0.05
    inss = salario_bruto * 0.1
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    descontos = inss + imposto_renda
    salario_liquido = salario_bruto - descontos

elif salario_bruto > 1500 and salario_bruto <= 2500:
    imposto_renda = salario_bruto * 0.1
    inss = salario_bruto * 0.1
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    descontos = inss + imposto_renda
    salario_liquido = salario_bruto - descontos

elif salario_bruto > 2500:
    imposto_renda = salario_bruto * 0.2
    inss = salario_bruto * 0.1
    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    descontos = inss + imposto_renda
    salario_liquido = salario_bruto - descontos

print(f"Salario Bruto:      R$ {salario_bruto:.2f}")
print(f"Desconto sindicato: R$ {sindicato:.2f}")
print(f"IR:                 R$ {imposto_renda:.2f}")
print(f"INSS:               R$ {inss:.2f}")
print(f"FGTS:               R$ {fgts:.2f}")
print(f"Total descontos:    R$ {descontos:.2f}")
print(f"Salario Liquido:    R$ {salario_liquido:.2f}")

