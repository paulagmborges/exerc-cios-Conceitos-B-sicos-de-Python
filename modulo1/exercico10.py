#Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas.
#Exemplos de variáveis:nome,idade,lugar,profissão....
#Exemplo de retorno:Olá Maria,prazer te conhecer.Sou de São Paulo também estou migrando de área.


nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")
profissaoAtual = input("Digite sua profisão atual: ")
profissao = input("Digite a profissão que pretende migrar: ")


mensagem = f"Olá {nome}, prazer em te conhecer. Tenho {idade} anos e sou de {cidade}. Atualmente, trabalho como {profissaoAtual} e estou migrando para a área de {profissao}."
print(mensagem)
