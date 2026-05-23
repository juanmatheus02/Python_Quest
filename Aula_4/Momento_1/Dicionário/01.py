'''1. Elabore um sistema em que seja possível:
• Cadastrar nome do funcionário e seu salário
• Listar todos os funcionários cadastrados
• Remover um funcionário pelo nome informado
Ao remover um funcionário, o salário correspondente também deve ser removido da
lista.'''

funcionário_salario = []
for i in range(2):
    funcionário = input(f"Nome do funcionário {i + 1}: ")
    salario = float(input(f"Salário do funcionário {i+1}: "))

    func_sala = {
        "Funcionário": funcionário,
        "Salário": salario
    }

    funcionário_salario.append(func_sala)
print(funcionário_salario)

remover_funcionário = str(input("Qual funcionário deseja remover? "))
for funcionário in funcionário_salario:
    if funcionário ["Funcionário"] == remover_funcionário:
        funcionário_salario.remove(funcionário)
        break
print(funcionário_salario)