# Faça um programa,com uma função que necessite de três argumentos,e que forneça a soma desses três argumentos.

def somaTresArgumentos(argumento1, argumento2, argumento3):
    resultado = argumento1 + argumento2 + argumento3
    return resultado

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


soma = somaTresArgumentos(num1, num2, num3)
print(f"A soma dos três números é: {soma}")
