#7. Calculadora Simples

print("====Calculos Matematicos====\n")
print("Intituto Albert Einstein\n")
print("1 - Soma(+)\n2 - Subtração(-)\n3 - Multiplicação(*)\n4 - Divisão(/)\n5 - Saír")
operacao = input("Digite qual operação deseja: ").lower()

match operacao:
    case "1" | "soma" | "+":
        print("Soma Escolhida !!!")
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        calculo = n1 + n2
        print(f"O resultado da sua soma é: {calculo:.2f}")

    case "2" | "subtração" | "subtracao" | "-":
        print("Subtração Escolhida !!!")
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        calculo = n1 - n2
        print(f"O resultado da sua subtração é: {calculo:.2f}")

    case "3" | "multiplicacao" | "multiplicação" | "*":
        print("Multiplicação Escolhida !!!")
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        calculo = n1 * n2
        print(f"O resultaodo da sua multiplicação é: {calculo:.2f}")

    case "4" | "divisao" | "divisão" | "/":
        print("Divisão Escolhida")
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        calculo = n1 / n2
        print(f"O resultado da sua divisão é: {calculo:.2f}")

    case "5" | "sair" | "saír":
        print("Saindo de Calculos Matematicos!!!")
    case _:
        print("Opção Invalida!!!!")