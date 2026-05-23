'''2. Elabore um sistema em que seja possível:
• Cadastrar nome do produto
• Cadastrar a quantidade em estoque
• Cadastrar o valor de cada produto
• Listar todos os produtos cadastrados mostrando nome, quantidade e valor
• Remover um produto pelo nome informado
Ao remover um produto, a quantidade e o valor correspondentes também devem ser
removidos das listas para manter o controle correto do estoque.'''

produtos = []
estoque = []
valores = []

for i in range (2):
    novo_produto = str(input(f"Digite o produto {i + 1}: "))
    produtos.append(novo_produto)
    qtde_estoque = int(input(f"Quantos itens do produto {i + 1} tem no estoque? "))
    estoque.append(qtde_estoque)
    valor = float(input(f"Qual valor do produto {i + 1}? "))
    valores.append(valor)

print(f"Produtos: {produtos}")
print(f"Estoque: {estoque}")
print(f"Valores: {valores}")

remover_produto = str(input("Qual produto deseja remover? "))
if remover_produto in produtos:
    indice = produtos.index(remover_produto)
    produtos.pop(indice)
    estoque.pop(indice)
    valores.pop(indice)

print(f"Produtos: {produtos}")
print(f"Estoque: {estoque}")
print(f"Valores: {valores}")