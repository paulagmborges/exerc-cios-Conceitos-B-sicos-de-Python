# Implemente um programa que classifique um aluno com base em sua pontuação em um exame.
#O programa deverá solicitar uma nota de 0 a 10.
#Se a pontuação for maior ou igual a 7,o aluno é aprovado;caso contrário,é reprovado.

nota = float(input("Digite a sua nota do exame de 0 a 10: "))

if nota >= 7:
 print('aprovado')
else :
    print('reprovado')