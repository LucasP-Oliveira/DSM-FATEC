#Peça um número ao usuário e exiba sua tabuada de 1 a 10, mas se for múltiplo de 3, substitua pelo texto "Multiplo de 3".

num = int(input("Digite um numero: "))
print("Tabuada")

for i in range(1, 11):
    if num % 3 == 0:
        print(f"O numero {num} é multiplo de 3!!")
        break
    else:
        print(f"{num} x {i} = {num * i}")

