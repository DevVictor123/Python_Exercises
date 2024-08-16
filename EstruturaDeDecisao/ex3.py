#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra = input("Selecione o sexo (F ou M): ")

if letra.upper() == 'M':
    print("Masculino")

elif letra.upper() == 'F':
    print("Feminino")

else:
    print("Sexo invalido")