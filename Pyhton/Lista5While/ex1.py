numeros = int(input("Digite um numero: "))
soma = 0

while numeros != 0:
    soma += numeros
    numeros = int(input("Digite outro numero: "))

print("A soma dos numeros: ", soma)