calculo = input("Digite que tipo de calculo deseja realizar (a - adição, s - subtração, d - divisão, m - multiplicação): ")
num1 = int(input("Digite o primerio numero: "))
num2 = int( input("Digite o segundo numero: "))

adicao = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2

if calculo == "a":
    print(f"A soma dos valores {num1} e {num2} é: {adicao}")
elif calculo == "s":
    print(f"A soma dos valores {num1} e {num2} é: {subtracao}")
elif calculo == "d":
    print(f"A soma dos valores {num1} e {num2} é: {divisao}")
elif calculo == "m":
    print(f"A soma dos valores {num1} e {num2} é: {multiplicacao}")