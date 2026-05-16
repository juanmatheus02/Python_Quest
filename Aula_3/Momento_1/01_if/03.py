"""3. Crie uma função chamada desconto() 
que receba o valor de um produto. 
SE pagamento for em PIX 10% de desconto, 
SE cartão, perguntar parcelamento. 
Até 3x sem juros, acima disso, aplicar 5%"""

def desconto(produto, pagamento):
    porcentagem = (produto*10)/100
    desconto_pix = produto - porcentagem
    return porcentagem, desconto_pix

produto = float(input ("Valor do produto: "))
pagamento = input("Digite a forma de pagamento, P - Pix, C - Cartão")

if pagamento == P:
    print(desconto_pix)
    