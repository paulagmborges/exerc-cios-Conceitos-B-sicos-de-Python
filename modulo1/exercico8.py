#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.


valorPorHora = float(input("Digite quanto você ganha por hora: "))
nHorasTrabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))


salario = valorPorHora * nHorasTrabalhadas



print(f"Seu salário no mês é: R${salario:.2f}")

