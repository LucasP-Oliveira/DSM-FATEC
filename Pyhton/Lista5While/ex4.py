# Faça um programa que converta uma temperatura de Celsius para Fahrenheit. Continue pedindo ao usuário para inserir uma nova temperatura em Celsius até que ele digite "sair".
opcao = input("Digite continue ou sair: ")

while opcao != "sair":
    opcao = input("Digite a temperatura a ser convertida: ")

    if opcao == "sair":
        print("Saindo do programa ")

    else:
        opcao = int(opcao)
        fahrenheit = (opcao * 1.8) + 32
        print(f"A temperatura em Celsius: {opcao} equivale a {fahrenheit} Fahrenheit")