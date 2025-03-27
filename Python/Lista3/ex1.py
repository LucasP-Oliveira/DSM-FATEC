while True:

    print("====== Conversor ======")
    print("1 - Dolár(USD)")
    print("2 - Euro(EUR)")
    print("3 - Libra(GBP)")
    print("4 - Sair")

    conversorMoeda = input("Escolha para qual moeda deseja converter o Real: ").lower()

    match conversorMoeda:
        case "dolar":
            print(f"Selecionando: { conversorMoeda }")
            valor = float(input("Digite o valor que deseja converter: "))
            dolar = valor * 5.69
            print(f"O valor: $ {valor} convertido para reais, é : R$ {dolar:.2f} ")
            break
        case "euro":
            print(f"Selecionando: { conversorMoeda }")
            valor = float(input("Digite o valor que deseja converter: "))
            euro = valor * 6.20
            print(f"O valor: € {valor} convertido para reais, é : R${euro:.2f} ")
            break
        case "libra":
            print(f"Selecionando: {conversorMoeda}")
            valor = float(input("Digite o valor que deseja converter: "))
            libra = valor * 7.37
            print(f"O valor: £ {valor} convertido para reais, é : R${libra:.2f} ")
            break
        case "sair":
            print("Saindo do programa!!")
            break

        case _:
            print("opção invalida!!")
            