# Escreva um programa que calcule o tempo de uma viagem.
#Faça um comparativo do mesmo percurso de avião,carro e ônibus.
#Levando em consideração:
#●avião=600km/h
#●carro=100km/h
#●ônibus=80km/h7



distancia = float(input("Informe a distância da viagem em quilômetros: "))
velocidade= float(input("Informe a velocidade em horas : "))
calculoTempo = distancia / velocidade

velocidadeAviao = 600
tempoAviao = calculoTempo

velocidadeCarro = 100
tempoCarro = calculoTempo

velocidadeOnibus = 80
tempoOnibus = calculoTempo

print(f"Tempo de viagem de avião: {tempoAviao:.2f} horas")
print(f"Tempo de viagem de carro: {tempoCarro:.2f} horas")
print(f"Tempo de viagem de ônibus: {tempoOnibus:.2f} horas")


