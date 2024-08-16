#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite um letra: ")

if letra.isdigit():
    print("invalido")

elif letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vogal")

else:
    print("Consoante")