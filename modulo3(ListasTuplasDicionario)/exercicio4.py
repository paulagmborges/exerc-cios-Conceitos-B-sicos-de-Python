# Crie um dicionário representando contatos(nome,telefone).
#Permita ao usuário procurar por um contato pelo nome.

contatos={
'Danielle': '123-4567',
'João' : '1234- 76543',
'Pamela' : '1234-9583',
'Amanda' : '1234-82762',
}

telefone = 0

nomeProcurado = input("Digite o nome do contato para procurar: ")

for contato, numero in contatos.items():
    if contato == nomeProcurado:
        telefone = numero
        print(f"Telefone de {nomeProcurado}: {telefone}")
        break
else:
    print(f"O contato {nomeProcurado} não foi encontrado.")



