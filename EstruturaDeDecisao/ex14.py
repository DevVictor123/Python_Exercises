#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:Média de Aproveitamento Conceito Entre 9.0 e 10.0 A; Entre 7.5 e 9.0 B; Entre 6.0 e 7.5 C; Entre 4.0 e 6.0 D Entre 4.0 e zero E; O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media <= 10.0 and media > 9.0:
    conceito = 'A'

elif media <= 9.0 and media > 7.5:
    conceito = 'B'

elif media <= 7.5 and media > 6.0:
    conceito = 'C'

elif media <= 6.0 and media > 4:
    conceito = 'D'

elif media <= 4 and media > 0:
    conceito = 'E'

print(f"Notas: {nota1} e {nota2}")
print(f"Media: {media:.2f}")
print(f"Conceito {conceito}")
conceitos = {'A': 'APROVADO', 'B': 'APROVADO', 'C': 'APROVADO', 'D': 'REPROVADO', 'E': 'REPROVADO'}
print(f"Resultado: {conceitos[conceito]}")



