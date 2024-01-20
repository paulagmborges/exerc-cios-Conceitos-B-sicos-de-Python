# Criar um programa em Python que solicite três números ao usuário,utilize estruturas condicionais para determinar o maior entre eles e apresent e o resultado.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print ('Número 1 é maior')
elif numero2 > numero1 and numero2 > numero3:
    print('Número 2 é maior')
else:
    print ('Número 3 é o maior')
