#Simulador de Compra em Loja Online

print("==Vendas de Video Games==")
print("Produtos Disponiveis:\n1 - PLaystation1\n2 - PLaystation2\n3 - PLaystation3\n4 - PLaystation4\n5 - PLaystation5")
print("6 - Xbox360\n7 - XboxOne\n8 - XboxOne X/S\n9 - Xbox Series X/S")
print("10 - Nintendo Switch\n11 - Saír")

produto = input("Digite qual produto deseja saber o preço: ").lower()
match produto:
    case "1" | "playstation1" | "play1" | "ps1":
        print("Bom o Playstation1 está no valor de: R$349,00")
    case "2" | "playstation2" | "play2" | "ps2":
        print("Bom o Playstation2 está no valor de: R$588,00")
    case "3" | "playstation3" | "play3" | "ps3":
        print("Bom o Playstation3 está no valor de: R$1.199,00")
    case "4" | "playstation4" | "play4" | "ps4":
        print("Bom o Playstation4 está no valor de: R$2.199,00")
    case "5" | "playstation5" | "play5" | "ps5":
        print("Bom o Playstation5 está no valor de: R$4.072,84")
    case "6" | "xbox360" | "x360":
        print("Bom o Xbox360 está no valor de: R$1000,00")
    case "7" | "xboxone" | "xone":
        print("Bom o XboxOne está no valor de: R$2.099,00")
    case "8" | "xboxone x/s" | "xone x" | "xone s" | "xboxone x" | "xboxone s":
        print("Bom o XboxOne X/S está no valor de: R$2.100,00")
    case "9" | "xbox series x/s" | "xbox series s" | "xbox series x":
        print("Bom o Xbox Series S/X está no valor de: R$2.799,00")
    case "10" | "switch" | "nintendo" | "nintendo switch":
        print("Bom o Nintendo Switch está no valor de: R$ 1.893,79")
    case "11" | "sair" | "saír":
        print("Saindo do Programa")
    case _:
        print("Produto não disponivel!!")
