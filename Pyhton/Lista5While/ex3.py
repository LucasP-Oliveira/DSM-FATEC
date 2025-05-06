positivo = 0
negativo = 0
zero = 0
count_posi = 1
count_nega = 1
count_zero = 1
i = 0

while True:
    i += 1
    valores = input(f"Digite o numero {i}: ")

    if valores == "sair":
        break

    valores = int(valores)

    if valores > 0:
        positivo += count_posi

    elif valores < 0:
        negativo += count_nega

    else:
        zero += count_zero

print("tabela de valores")
print(f"O total de numeros positivos: {positivo}")
print(f"O total de numeros negativos: {negativo}")
print(f"O total de numeros zeros: {zero}")


