
#Solicite ao usuário o número de horas d eexercício físico por semana.
#Calcule o total de calorias queimadas em um mês,considerando uma média de 5 calorias por minuto de exercício.


horasSemana = float(input("Digite o número de horas de exercício físico por semana: "))


minutosPorSemana = horasSemana * 60

#
minutosPorMes = minutosPorSemana * 4  


caloriasPorMin = 5
caloriasTotais = minutosPorMes * caloriasPorMin

# Exibe o resultado
print(f"Total de calorias queimadas em um mês: {caloriasTotais} calorias")
