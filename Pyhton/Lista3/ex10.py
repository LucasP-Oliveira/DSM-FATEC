#Sistema de Pagamento
print("===Sistema de pagamentos===\n")
print("Tipos de Pagamentos:")
print("1 - Debito\n2 - Credito\n3 - Pix\n4 - Boleto\n5 - Cheque\n6 - Saír")

opcao = input("Escolha o tipo de pagamento para saber\nse a desconto ou acréscimo no valor ao pagar:  ")

match opcao:
    case "1" | "debito" | "débito":
        print("\n===PAGAMENTO NO DEBITO===")
        print("Ao realizar o Pagamento no debito Você recebe 15% de desconto!!")

    case "2" | "credito" | "crédito":
        print("\n===PAGAMENTO NO CREDITO===")
        print("Ao realizar o Pagamento no credito Você recebe 15% de  acrescimo!!")

    case "3" | "Pix":
        print("\n===PAGAMENTO NO PIX===")
        print("Ao realizar o Pagamento no pix Você recebe 25% de desconto!!")

    case "4" | "Boleto" :
        print("\n===PAGAMENTO NO BOLETO===")
        print("Ao realizar o Pagamento no Boleto Você recebe 5% de acrescimo!!")

    case "5" | "cheque":
        print("\n===PAGAMENTO NO CHEQUE===")
        print("Ao realizar o Pagamento no cheque Você recebe 10% de acrescimo!!")

    case "6" | "sair" | "saír":
        print("Saindo do Sistema de Pagamentos")
    case _:
        print("Tipo de Pagamento Invalido!!!!")