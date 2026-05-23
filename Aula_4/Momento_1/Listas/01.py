'''1. Elabore um sistema em que seja possível:
• Cadastrar nome do funcionário e seu salário
• Listar todos os funcionários cadastrados
• Remover um funcionário pelo nome informado
Ao remover um funcionário, o salário correspondente também deve ser removido da
lista.'''

funcionarios = []
salarios = []

for i in range (2):
    funcionario = str(input(f"Digite o nome do Funcionário {i + 1}: "))
    funcionarios.append(funcionario)
    salario = float(input(f"Digite o Salário do Funcionário {i + 1}: "))
    salarios.append(salario)

print(funcionarios)
print(salarios)

remover_funcionário = str(input("Qual funcionário deseja remover? "))
if remover_funcionário in funcionarios:
    indice = funcionarios.index(remover_funcionário)
    funcionarios.pop(indice)
    salarios.pop(indice)

print(funcionarios)
print(salarios)


