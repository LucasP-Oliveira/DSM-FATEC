#Peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

num = int(input("Digite um numero: "))
if num > 0:
    print("Tabuada")
    for i in range(1,11):

        print(f"{num} x {i} = {num * i}")
else:
    print("Erro!!")