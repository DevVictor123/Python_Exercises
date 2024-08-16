#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano = int(input("Digite um ano (xxxx): "))

dezena = ano % 100

if dezena % 4 == 0:
    print("ano bisexto")
if dezena == 0:
    if ano % 400 == 0:
        print("ano bisexto")

else:
    print("Ano NAO e bisexto")

