preco = float(input("DIgite o valor do produto: "))
desconto = 0.10 * preco


if preco > 100:
    print("Voce ganhou em desconto")
    valor = preco - desconto
    print(f"O valor totala pagar é: {valor}")
else:
    print(f"Total a pagar: {preco}")
