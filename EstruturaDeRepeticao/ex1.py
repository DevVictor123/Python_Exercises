#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
num = float((input("Digite um numero entre 0 e 10: ")))

while(True):
    if num <= 0 or num > 10:
        print("Numero informado invalido")
        num = float(input("Digite um numero entre 0 e 10: "))
    else:
        break
        