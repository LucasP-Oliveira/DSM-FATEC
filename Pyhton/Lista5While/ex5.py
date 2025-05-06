#Crie um programa que simule um caixa eletrônico, que continue pedindo ao usuário para inserir um valor de saque até que o saldo da conta seja zero ou negativo.

saldo = float(input("Digite o seu saldo: "))
print(saldo)

while True:
    saque = float(input("Digite o valor a sacar: "))

    if saque > saldo:
        print(f"Valor de saque: {saque} inválido pois não tem saldo sulficiente")

    elif saldo != 0:
        saldo -= saque
        print(f"Apos o saque o seu saldo ficou de: {saldo}")
        if saldo == 0:
            print("Finalizando Programa!!")
            break


