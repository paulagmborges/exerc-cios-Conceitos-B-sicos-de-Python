# Faça umprograma que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
#Dica:lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

usuario = input("Digite o seu nome: ")

usuarioModificado = usuario[::-1].upper()

print("Nome invertido:", usuarioModificado)
