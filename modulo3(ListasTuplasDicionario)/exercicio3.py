#Crie um dicionário representando um carrinho de compras.
#Adicione produtos(chaves) e quantidades(valores) ao carrinho.
#Calcule o total do carrinho de compra 

carrinhoDeCompras = {}

carrinhoDeCompras['arroz'] = 3
carrinhoDeCompras['feijao'] = 2
carrinhoDeCompras['leite'] = 1
carrinhoDeCompras['biscoito'] = 2

precos = {'arroz': 6.5, 'feijao': 9.0, 'leite': 4.0, 'biscoito': 2.0}

total = sum(carrinhoDeCompras[produto] * precos[produto] for produto in carrinhoDeCompras)
print("Carrinho de Compras: ")

for produto, quantidade in carrinhoDeCompras.items():
    print(f"{produto}: {quantidade} unidades")

print(f"\nTotal do Carrinho de Compras: R${total:.2f}")

