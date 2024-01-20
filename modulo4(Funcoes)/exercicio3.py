# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa.
#Para cada opção,crie uma função.

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Escolha a opção de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        temperatura = float(input("Digite a temperatura em graus Celsius: "))
        resultado = celsius_para_fahrenheit(temperatura)
        unidade_destino = "Fahrenheit"

    elif escolha == "2":
        temperatura = float(input("Digite a temperatura em graus Fahrenheit: "))
        resultado = fahrenheit_para_celsius(temperatura)
        unidade_destino = "Celsius"

    else:
        print("Escolha inválida. Por favor, digite 1 ou 2.")
        return

    print(f"A temperatura convertida é: {resultado:.2f}°{unidade_destino}")

if __name__ == "__main__":
    main()

