'''
2. Desenvolva um sistema simples de autenticação. O programa deve solicitar ao usuário um login e uma senha. 
Enquanto o login estiver incorreto ou a senha estiver incorreta, o sistema deve informar que os dados estão errados
e solicitar novamente as  informações. Quando o usuário digitar corretamente o login e a senha, 
o sistema deve encerrar o loop e exibir a mensagem de acesso liberado.

Observação: login = "admin " e senha= "1234"
'''

login_cadastrado = "admin"
senha_cadastrada = "1234"

login = str(input("Digite o Login: "))
while login != login_cadastrado:
    print("Login incorreto!")
    login = str(input("Digite o Login novamente: "))
senha = str(input("Digite a senha: "))
while senha != senha_cadastrada:
    print("Senha incorreta!")
    senha = str(input("Digite a senha novamente: "))

print("Acesso Liberado")
