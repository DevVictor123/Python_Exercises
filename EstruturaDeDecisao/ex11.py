#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:salários até R$ 280,00 (incluindo) : aumento de 20%salários entre R$ 280,00 e R$ 700,00 : aumento de 15%salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:o salário antes do reajuste;o percentual de aumento aplicado;o valor do aumento;o novo salário, após o aumento.
salario_atual = float(input("Digite o salário atual: "))

if salario_atual <= 280:
    aumento_percentual = 20 / 100
    aumento = salario_atual * aumento_percentual
    novo_salario = salario_atual + aumento

elif salario_atual > 280 and salario_atual < 700:
    aumento_percentual = 15 / 100
    aumento = salario_atual * aumento_percentual
    novo_salario = salario_atual + aumento

elif salario_atual > 700 and salario_atual < 1500:
    aumento_percentual = 10 / 100
    aumento = salario_atual * aumento_percentual
    novo_salario = salario_atual + aumento

elif salario_atual > 1500:
    aumento_percentual = 5 / 100
    aumento = salario_atual * aumento_percentual
    novo_salario = salario_atual + aumento

print(f"Salário antes reajuste: R${salario_atual:.2f}")
print(f"Percentual aplicado: {aumento_percentual * 100}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")
