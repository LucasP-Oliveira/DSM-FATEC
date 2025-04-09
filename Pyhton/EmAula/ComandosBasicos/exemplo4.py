
operacao = input("Digite o que deseja realizar (saque, deposito, saldo ): ")
banco = 1000

if operacao == "saque":
    print("Realizando saques!!")
    valorS = float(input("Digite o valor a sacar: "))
    if valorS > banco:
        print("Saldo insulficiente para saque")
    else:
        print("Saque realizado com sucesso!")
        bancoSaque = banco - valorS
        print(f"Resta no banco: {bancoSaque}")

elif operacao == "deposito":
    print("Realizando deposito!!")
    valorD = float(input("Digite o valor a depositar: "))
    bancoDeposito = banco + valorD
    print(f"Valor no banco: {bancoDeposito}")

elif operacao == "saldo":
    print(f"O total que voce possui no banco é de: {banco}")

else:
    print("Operação invalida!!!!")
