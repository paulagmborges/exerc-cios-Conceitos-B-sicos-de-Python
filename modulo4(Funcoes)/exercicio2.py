# Reverso do número.Faça uma função que retorne o reverso de um número inteiro informado.Por exemplo: 127->721.

def inverterNumero(numero):
    numeroInvertido = 0

    while numero > 0:
        digito = numero % 10
        numeroInvertido = numeroInvertido * 10 + digito
        numero = numero // 10

    return numeroInvertido

numeroOriginal = int(input("Digite um número inteiro: "))

numeroInvertido = inverterNumero(numeroOriginal)
print(f"O número invertido é: {numeroInvertido}")
