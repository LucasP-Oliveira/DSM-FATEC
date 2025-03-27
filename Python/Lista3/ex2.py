while True:
    print("==== Calculo de Area ====")
    print("1 - Quadrado")
    print("2 - Triangulo")
    print("3 - Retangulo")
    print("4 - sair")

    forma = input("Escolha qual a forma que deseja calcular a area: ").lower()

    match forma:
        case "1" | "quadrado":
            print(f"Selecionando Quadrado")
            l1 = float(input("Digite o valor do lado 1: "))
            l2 = float(input("Digite o valor do lado 2: "))
            area = l1 * l2
            print(f"A area do Quadrado é: {area} ")

        case "2" | "triangulo" :
            print("Selecionando Triangulo")
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))
            area = (base * altura) / 2
            print(f"A area do Triangulo é: {area} ")

        case "3" | "retangulo" | "retângulo":
            print("Selecionando Retângulo")
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))
            area = base * altura
            print(f"A area do Retângulo é: {area} ")

        case "4" | "sair" | "saír":
            print("Saindo do Programa!!")
            break

        case _:
            print("Opção invalida")
