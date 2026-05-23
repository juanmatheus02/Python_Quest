'''2. Elabore um sistema em que seja possível:
• Cadastrar nome do produto
• Cadastrar a quantidade em estoque
• Cadastrar o valor de cada produto
• Listar todos os produtos cadastrados mostrando nome, quantidade e valor
• Remover um produto pelo nome informado
Ao remover um produto, a quantidade e o valor correspondentes também devem ser
removidos das listas para manter o controle correto do estoque.'''

dados = []
for i in range(2):
    produto = str(input(f"Produto {i + 1}: "))
    estoque = int(input(f"Quantidade no estoque {i + 1}: "))
    valor = float(input(f"Quanto que vale {i + 1}: "))

    dicionário = {
        "Produto": produto,
        "Estoque": estoque,
        "Valor": valor
    }
    dados.append(dicionário)

print(dados)

remover_produto = str(input("Qual produto deseja remover? "))
for produtos in dados:
    if produtos["Produto"] == remover_produto:  
        dados.remove(produtos)
        break

print(dados)