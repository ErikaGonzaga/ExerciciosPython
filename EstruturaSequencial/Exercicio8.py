# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_por_hora = float(input("Informe quanto ganha por hora\n"))
qtd_horas_trabalhadas_mes = int(input("Informe a quantidade de horas trabalhadas no mês\n"))

salario = valor_por_hora * qtd_horas_trabalhadas_mes

print("O total do salário do mês é:",salario)