#Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de    1,5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
pop_A = 80000
pop_B = 200000
anos = 1

taxa_crescimento_A = (0.03 * pop_A) + pop_A

taxa_crescimento_B = (0.015 * pop_B) + pop_B


while taxa_crescimento_A <= taxa_crescimento_B:
    taxa_crescimento_A += (0.03 * taxa_crescimento_A) 
    taxa_crescimento_B += (0.015 * taxa_crescimento_B)
    anos += 1

print(f"levara: {anos} anos")
    


