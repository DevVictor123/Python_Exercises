#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
pop_A = int(input("Digite a populacao A: "))
pop_B = int(input("Digite A populacao B: "))

while(True):
    if pop_A > pop_B:
        print("a populacao da cidade A deve ser menor que da cidade B")
        pop_A = int(input("Digite a populacao A: "))
        pop_B = int(input("Digite A populacao B: "))
    else:
        break

anos = 1

taxa_crescimento_A = (0.03 * pop_A) + pop_A
taxa_crescimento_B = (0.015 * pop_B) + pop_B

while taxa_crescimento_A <= taxa_crescimento_B:
    taxa_crescimento_A += (0.03 * taxa_crescimento_A) 
    taxa_crescimento_B += (0.015 * taxa_crescimento_B)
    anos += 1

print(f"levara: {anos} anos")