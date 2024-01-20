# Faça um Programa que peça as quatro notas de 5 alunos,calcule e armazene numa lista a média de cada aluno,imprima o número de alunos com média maior ou igual a 7.

mediaDeAlunos = []

for i in range(5):
    notas = [float(input(f"Digite a nota {j + 1} do aluno {i + 1}: ")) for j in range(4)]

    media = sum(notas) / len(notas)
    mediaDeAlunos.append(media)
print("Médias dos alunos:", mediaDeAlunos)


alunosAprovados = sum(1 for media in mediaDeAlunos if media >= 7.0)

print(f"Número de alunos com média maior ou igual a 7.0: {alunosAprovados}")
