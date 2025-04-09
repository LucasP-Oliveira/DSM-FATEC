#Solicite um número ao usuário e exiba o seu fatorial (n!).

num = int(input("Digite um numero: "))
fator = 1
for i in range(1, num + 1):
    fator *= i
print(f"O fatorial de {num}: {fator} ")