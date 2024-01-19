# Faça um Programa que peça a quantidade de quilômetros,transforme em metros,centímetros e milímetros


km = float(input("Digite a quantidade de quilômetros: "))

metros = km * 1000

centimetros = km * 100000

milimetros = km * 1000000


print(f"{km} quilômetros são equivalentes a:")
print(f"{metros} metros")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")
