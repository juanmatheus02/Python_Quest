'''
1. Crie um programa que peça números ao usuário e vá somando esses valores. 
Enquanto a soma for menor que 100, o programa deve continuar pedindo novos números
e exibindo a soma atual.  Quando atingir ou ultrapassar 100, o programa deve encerrar
e mostrar uma mensagem final.
'''

soma = 0
num = 0
num2 = 0
while soma <100:
    num = int(input("Diga um número para somar: "))
    num2 = int(input("Diga o próximo número para somar: "))
    soma = num + num2
    print(soma)

