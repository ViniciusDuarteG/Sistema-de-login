nome = str
email = str
senha = str
confirmacao_senha = str

escolha = 9

usuario_cadastrado={'nome':'','senha':'','email':''}

def SistemaLogin():
    email = str(input("E-mail:\n"))
    senha = str(input("Senha:\n"))
    if email == usuario_cadastrado['email'] and senha == usuario_cadastrado['senha']:
        print("Bem vindo!")
    else:
        print("Senha incorreta")

def SistemaRegistro():
    nome = str(input("Digite seu nome:\n"))
    usuario_cadastrado['nome'] = nome
    email = str(input("Digite seu email:\n"))
    usuario_cadastrado['email'] = email
    
    senha = str(input("Digite a senha: "))
    confirmacao_senha = str(input("Confirme a sua senha: "))
    if senha == confirmacao_senha:
        usuario_cadastrado['senha'] = senha
        print('\n')
        print("Usuário cadastrado.")
        print('\n')
    
    while senha != confirmacao_senha:
        print("Senha divergente, tente novamente.")
        senha = str(input("Digite a senha: "))
        confirmacao_senha = str(input("Confirme a sua senha: "))

        


while escolha != 3:
    escolha = int(input("Oque você deseja fazer:\n1-Login\n2-Registrar-se\n0-Sair\n"))
    if escolha == 1:
        SistemaLogin()
    elif escolha == 2:
        SistemaRegistro()
    elif escolha == 0:
        print(usuario_cadastrado)
    
