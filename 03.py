"""5. Desenvolva um sistema de caixa com while True para uma loja com três produtos fixos: 
feijão (R$ 8,00), arroz (R$ 6,50) e farinha (R$ 5,00). 
O programa deve permitir registrar vendas, somar o total vendido e encerrar quando o usuário escolher sair."""

feijao = 8
arroz = 6.50
farinha = 5

total = 0 

while True:
    quantidadeFE = int(input("Quantos feijões você quer? "))
    somaF = quantidadeFE * feijao

    quantidadeA = int(input("Quantos arroz você quer? "))
    somaA = quantidadeA * arroz

    quantidadeFA = int(input("Quantas farinhas você quer? "))
    somaFA = quantidadeFA * farinha

    total += somaF + somaA + somaFA

    print(f"Subtotal acumulado: R$ {total:.2f}")

    sair = input("Deseja continuar? Digite 1 para continuar e 2 para sair: ")
    if sair == "2":
        print(f"Total final: R$ {total:.2f}")
        break



