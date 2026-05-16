"""2. Crie uma função chamada comissao() 
que receba o valor total das
vendas e retorne 10% desse valor. 
Depois, mostre o resultado final."""

def comissao():
    a = float(input("Valor total das vendas: "))
    porcentagem = (a*10)/100
    total = a + porcentagem
    print("Sua comissão é de: ",porcentagem, "Totalizando: ",total)

comissao()