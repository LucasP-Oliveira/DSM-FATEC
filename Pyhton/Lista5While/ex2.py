entrada = input("Digite um numero: ")
if entrada != "sair":
    numero = int(entrada)
    maior = numero
    menor = numero

    while True:
        entrada = input("Digite outro numero(ou sair para finalizar o programa: ")
        if entrada == "sair":
            break

        numero = int(entrada)

        if numero > maior:
            maior = numero

        elif numero < menor:
            menor = numero

    print(f"O maior numero é: {maior}")
    print(f"O menor numero é: {menor}")