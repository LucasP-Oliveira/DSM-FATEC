#Peça ao usuário 10 números e exiba quantos são positivos, negativos ou zero.
positivo = 0
negativo = 0
zero = 0

for i in range(10):
    num = int(input("Digite um numero: "))
    if num > 0:
        positivo += i
    elif num < 0:
        negativo += i
    else:
        zero += i

print(f"Tem: {positivo} numeros positivos!")
print(f"Tem: {negativo} numeros negativo!")
print(f"Tem: {zero} numeros zero!")