"""3. Um sistema de caixa vai recebendo valores de compras de clientes. 
O operador digita os valores das compras. 
O sistema só para quando digitar o número 0 (zero), e no final mostra o total do dia"""

total = 0
while True:
    valor = float(input("Digite o valor da compra: "))
    total = valor + total
    print(total)
    if valor == 0:
        break
print(f"Subtotal {total}")