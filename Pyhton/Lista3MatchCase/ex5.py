#Tradutor de Cores
print("===== translate =====")
print("1 - Vermelho")
print("2 - Azul")
print("3 - Amarelo")
print("4 - Verde")
print("5 - Saír")

cor = input("Digite a cor : ").lower()

match cor:
    case "1" | "Vermelho ":
        print(f"A cor: Vermelho sendo feita a tradução fica: RED ")

    case "2" | "azul ":
        print(f"A cor: Azul sendo feita a tradução fica: BLUE ")

    case "3" | "amarelo ":
        print(f"A cor: Amarelo sendo feita a tradução fica: YELLOW ")

    case "4" | "verde ":
        print(f"A cor: Verde sendo feita a tradução fica: GREEN ")

    case "5" | "sair":
        print(f"Saindo !!!!")
