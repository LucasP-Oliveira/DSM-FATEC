#Solicite um número ao usuário e exiba a soma de 1 até esse número.

numero = int(input("Digite um numero: "))
soma = 0

for i in range(1, numero + 1):
   soma += i
print(soma)

