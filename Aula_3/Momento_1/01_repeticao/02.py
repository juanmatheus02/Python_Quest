"""Para as questões de 1 a 4
anteriormente realizadas, solicitar que
a pessoa usuária informe quantas vezes 
deseja realizar as operações e utilize 
o comando de repetição para realizar a
operação."""

def comissao():
    a = float(input("Valor total das vendas: "))
    porcentagem = (a*10)/100
    total = a + porcentagem
    print("Sua comissão é de: ",porcentagem, "Totalizando: ",total)

comissao()

vezes = int(input("Quantas vezes? "))

for i in range(vezes):
    a = float(input("Valor total das vendas: "))
    porcentagem = (a*10)/100
    total = a + porcentagem
    print("Sua comissão é de: ",porcentagem, "Totalizando: ",total)