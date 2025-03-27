while True:
    print("==== Produtos ====")
    print("1 - Eletrônicos")
    print("2 - Roupas")
    print("3 - Alimentos")
    print("4 - Móveis")

    produto = input("Digite qual opção de produto deseja: ")

    match produto:
        case "1" | "eletrônicos":
            print("Eletrônicos possuem 15% de desconto!!")
            break

        case "2" | "Roupas":
            print("Roupas possuem 5% de desconto!!")
            break

        case "3" | "Alimentos":
            print("Alimentos possuem 10% de desconto!!")
            break

        case "4" | "Móveis":
            print("Móvies possuem 30% de desconto")

        case _:
            print("Opção Inválida!!!")