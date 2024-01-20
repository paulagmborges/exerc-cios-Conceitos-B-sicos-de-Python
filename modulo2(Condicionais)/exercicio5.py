#Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero,isósceles ou escaleno.
#equilátero:todos os lados com  o mesmo valor 
#isósceles:dois lados com o mesmo valor 
#escaleno:todos os lados com medidas distintas.

comprimentoDoLado1 = float(input("Digite o comprimento do lado 1: "))
comprimentoDoLado2 = float(input("Digite o comprimento do lado 2: "))
comprimentoDoLado3 = float(input("Digite o comprimento do lado 3: "))

if comprimentoDoLado1 == comprimentoDoLado2 == comprimentoDoLado3:
    print('Equilétero')
elif comprimentoDoLado1==comprimentoDoLado2 or comprimentoDoLado2==comprimentoDoLado3 or comprimentoDoLado3==comprimentoDoLado1:
    print('Isóceles')
else:
    print('Escaleno')
