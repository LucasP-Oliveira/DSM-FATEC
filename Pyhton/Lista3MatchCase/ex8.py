#Sistema de Reserva de Passagens

print("===Reservas de Passagens===\n")
print("Aeroporto Viracopos\n")
print("Locais disponiveis:\n1 - São Paulo\n2 - Rio de Janeiro\n3 - Curitiba\n4 - Salvador\n5 - Saír")
local = input("Digite para onde deseja ir, de acordo com os locais diponiveis: ").lower()

match local:
    case "1" | "são paulo" | "sao paulo" | "sp":
        print("Local de destino desejado São Paulo!!!\n")
        print("Valor da passagem: R$178,00")

    case "2" | "rio de janeiro" | "rio" | "rj":
        print("Local de destino desejado Rio de Janeiro!!!\n")
        print("Valor da passagem ida e volta: R$%553,00 ")

    case "3" | "curitiba" | "pr":
        print("Local desejado Curitiba!!!\n")
        print("Valor da passagem ida e volta: R$623,00")

    case "4" | "salvador" | "ba":
        print("Local desejado Salvador!!!\n")
        print("Valor da passagem ida e volta: R$1.275,00")

    case "5" | "sair" | "saír":
        print("Saindo do Programa!!")
    case _:
        print("Local nao disponivel !!!")