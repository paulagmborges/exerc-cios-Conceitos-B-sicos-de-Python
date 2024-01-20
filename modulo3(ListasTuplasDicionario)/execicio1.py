# 1.Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntassão:""Telefonou para a vítima?""
#""Esteve no local do crime?""
#""Mora perto da vítima?""
#""Devia para a vítima?""
#""Já trabalhou coma vítima?""
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"",entre 3 e 4 como""Cúmplice""e 5 como""Assassino"".
#Caso contrário,ele será classificado como ""Inocente""

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostasSim = 0

for pergunta in perguntas:
    resposta = input(pergunta + " (Sim ou Não): ")
    if resposta.lower() == "sim":
      respostasSim += 1

if respostasSim == 2:
    print("A pessoa é Suspeita.")
elif 3 <= respostasSim <= 4:
    print("A pessoa é Cúmplice.")
elif respostasSim == 5:
    print("A pessoa é Assassino.")
else:
    print("A pessoa é Inocente.")
