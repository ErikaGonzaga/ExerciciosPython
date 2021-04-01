# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

graus_F = float(input("Informe a temperatura em graus Fahrenheit\n"))
graus_C = 5 * ((graus_F - 32) / 9)

print("A temperatura em graus Celsius é %.2f" %graus_C)