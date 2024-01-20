#Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e opercentual de desconto do Impostode Renda.
#●Renda até R$1.903,98 :isento de imposto de renda;
#●Renda entre R$ 1.903,99 e R$2.826,65:alíquotade7,5%;
#●Renda entre R$2.826,66 e R$3.751,05 : líquota de 15%;
#●Renda entre R$3.751,06 e R$4.664,68 : alíquota de 22,5%;
#●Renda acima de R$4.664,68 : alíquota máxima de 27,5%

salarioBruto = float(input("Digite o seu salário bruto: "))

if salarioBruto <= 1903.98:
    salarioLiquido = salarioBruto

elif 1903.99 <= salarioBruto <= 2826.65:
    taxa = (salarioBruto * 0.075)

elif 2826.66 <= salarioBruto <= 3751.05:
    taxa = (salarioBruto * 0.15)

elif 3751.06 <= salarioBruto <= 4664.68:
   taxa = (salarioBruto * 0.225)

else:  
   taxa = (salarioBruto * 0.275)

salarioLiquido = salarioBruto - taxa

print(f"Salário líquido: R${salarioLiquido:.2f}")
