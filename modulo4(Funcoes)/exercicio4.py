# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira,e calcule quanto poderia comprar de cada moeda estrangeira.
#Considere a tabelade conversão abaixo:
#DólarAmericano:R$4,91
#PesoArgentino:R$0,02
#DólarAustraliano:R$3,18
#DólarCanadense:R$3,64
#FrancoSuiço:R$0,42
#Euro:R$5,36
#Libraesterlina:R$6,215.


def converterMoedaEstrangeira(valorEmreais, taxaConversao):
    valorConvertido = valorEmreais/ taxaConversao
    return valorConvertido

def main():
    dinheiroEmReais = float(input("Digite a quantidade de dinheiro em reais na carteira: "))

    dolarAmericano = 4.91
    pesoArgentino = 0.02
    dolarAustraliano = 3.18
    dolarCanadense = 3.64
    francoSuico = 0.42
    euro = 5.36
    libraEsterlina = 6.21


    print(f"Com {dinheiroEmReais:.2f} reais, você poderia comprar:")
    print(f"Dólar Americano: ${converterMoedaEstrangeira(dinheiroEmReais, dolarAmericano):.2f}")
    print(f"Peso Argentino: ${converterMoedaEstrangeira(dinheiroEmReais, pesoArgentino):.2f}")
    print(f"Dólar Australiano: ${converterMoedaEstrangeira(dinheiroEmReais, dolarAustraliano):.2f}")
    print(f"Dólar Canadense: ${converterMoedaEstrangeira(dinheiroEmReais, dolarCanadense):.2f}")
    print(f"Franco Suíço: ${converterMoedaEstrangeira(dinheiroEmReais, francoSuico):.2f}")
    print(f"Euro: ${converterMoedaEstrangeira(dinheiroEmReais, euro):.2f}")
    print(f"Libra Esterlina: ${converterMoedaEstrangeira(dinheiroEmReais, libraEsterlina):.2f}")

if __name__ == "__main__":
    main()
