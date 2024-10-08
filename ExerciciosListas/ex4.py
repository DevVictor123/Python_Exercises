#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
texto = input("Digite uma frase (10 caracteres): ")

if len(texto) != 10:
    print("Erro: A frase deve conter 10 caractere")

else:
    qtd_consoantes = 0
    consoantes = []

    vogais = "aeiouAEIOU"
    
    for i in range(0, len(texto)):
        if texto[i] == " ":
            continue
        
        if texto[i] not in vogais:
            qtd_consoantes += 1
            consoantes.append(texto[i])
        
    print(f"Quantidade consoantes: {qtd_consoantes}")
    print(f"Consoantes: {''.join(consoantes)}")

