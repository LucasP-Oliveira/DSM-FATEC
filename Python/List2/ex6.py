usuarioCadastro = input("Digite o nome de usuario a ser cadastrado: ")
usuarioSenha = input("Digite a senha a ser cadastrada: ")

print("Cadastro realizado com sucesso!!")

while True:
    usuarioLogin = input("Digite o seu nome de usuario: ")
    if usuarioLogin != usuarioCadastro:
        print("usuario incorreto! ")
    else:
        usuarioSenhaLogin = input("Digite a senha: ")
        if usuarioSenhaLogin != usuarioSenha:
            print("senha incorreta!! ")
        else:
            print("Usuario Logado com sucesso!!")
