while True:
    print("==== Login ====\n")

    usuario = input("Digite o nome para o acesso: ").lower()

    match usuario:
        case "lucas" :
            print(f"{usuario} - Admin -> Acesso Total")
            break
        case "vitor":
            print(f"{usuario} - Professor -> Acesso ao ambiente acadêmico")
            break
        case _:
            print(f"{usuario} - Aluno -> Acesso ao ambiente de estudos")
            break


