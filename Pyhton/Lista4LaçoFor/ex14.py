#Peça ao usuário para digitar 5 números e exiba o maior e o menor deles.

num = int(input("Digite um número: "))
maior = num
menor = num


for i in range(1, 5):
    num = int(input("Digite outro número: "))

    if num > maior:
        maior = num

    if num < menor:
        menor = num

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")
