#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
dia = int(input("Digite um numero (1 a 7): "))

semana = {  1: 'Domingo', 2: 'Segunda', 3: 'Terca', 4: 'Quarta', 
            5: 'Quinta', 6: 'Sexta', 7: 'Sabado'}

if dia in semana:
    print(semana[dia])

else:
    print("valor invalido")