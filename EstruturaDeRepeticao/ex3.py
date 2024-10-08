#Faça um programa que leia e valide as seguintes informações: Nome: maior que 3 caracteres; Idade: entre 0 e 150; Salário: maior que zero; Sexo: 'f' ou 'm'; Estado Civil: 's', 'c', 'v', 'd';
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
sexo = input("Informe seu sexo (f ou m): ")
estado_civil = input("Informe seu estado civil (s, c, v, d): ")

valida = 0
while valida != 5:
    if len(nome) > 3:
        valida += 1
    else:
        print("O nome deve ser maior que 3 caracteres")
        nome = input("Informe seu nome: ")
    
    if idade > 0 or idade < 150:
        valida += 1
    else:
        print("A idade deve ser maior que 0 e menor que 150")
        idade = int(input("Digite sua idade: "))

    if salario > 0:
        valida += 1
    else:
        print("O salario deve ser maior que 0")
        salario = float(input("Digite seu salario: "))

    generos = ['f','m']
    
    if sexo.lower() in generos:
        valida += 1
    else:
        print("sexo invalido")
        sexo = input("Informe seu sexo novamente (f ou m): ")
    
    estados = ['s', 'c', 'v', 'd']
    
    if estado_civil.lower() in estados:
        valida += 1
    else:
        print("Estado civil invalido")
        estado_civil = input("Informe seu estado civil (s, c, v, d) novamente: ")
        

        
