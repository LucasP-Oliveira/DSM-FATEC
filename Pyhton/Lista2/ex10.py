operacao = input("Digite o que deseja realizar (saque, deposito): ")
banco: float = 1000.00


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
else:
    print("Operação invalida!!!!")
