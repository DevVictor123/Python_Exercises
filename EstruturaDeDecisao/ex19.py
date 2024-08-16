#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:326 = 3 centenas, 2 dezenas e 6 unidades; 12 = 1 dezena e 2 unidades
num = int(input("Digite um numero (max: 1000): "))

unidade = 0
dezena = 0
centena = 0

unidade = num % 10
dezena = (num % 100) // 10
centena = num // 100

if centena > 0:
    print(f"{centena} centenas, {dezena} dezenas e {unidade} unidades")

elif centena == 0 and dezena == 0:
    print(f"{unidade} unidades")

else:
    print(f"{dezena} dezenas e {unidade} unidades")