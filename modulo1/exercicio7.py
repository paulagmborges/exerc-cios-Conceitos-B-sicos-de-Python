#Solicite ao usuário o peso em kg e aaltura em metros.
#Calcule e imprima o Índice de Massa Corporal(IMC)
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

IMC=peso/(altura*altura)

print(f"O IMC é: {IMC:.2f} ")

