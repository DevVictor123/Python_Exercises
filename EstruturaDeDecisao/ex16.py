#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações: Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado; Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa; Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário; Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
from math import sqrt

coef_A = float(input("Digite o coeficiente A: "))

if coef_A == 0:
    print(" equação não é do segundo grau")
    exit()

coef_B = float(input("Digite o coeficiente B: "))
coef_C = float(input("Digite o coeficiente C: "))

delta = (coef_B ** 2) - 4 * coef_A * coef_C

if delta == 0:
    raiz = -coef_B / (2 * coef_A)
    print(f"Raiz unica {raiz:.2f}")

elif delta > 0:
    raiz_1 = (-coef_B + sqrt(delta)) / (2 * coef_A)
    raiz_2 = (-coef_B - sqrt(delta)) / (2 * coef_A)
    print(f"Raiz 1: {raiz_1:.2f}")
    print(f"Raiz 2: {raiz_2:.2f}")

else:
    print("não há raízes reais")
