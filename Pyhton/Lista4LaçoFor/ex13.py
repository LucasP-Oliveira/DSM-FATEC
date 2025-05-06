#Peça um número ao usuário e some separadamente os pares e os ímpares de 1 até esse número.

num = int(input("Digite um numero: "))
somapar = 0
somaimpar = 0
for i in range(1, num):
    if i % 2 == 0:
        print(f"{i} é par")
        somapar += i

    else:
        print(f"{i} é impar")
        somaimpar += i

print(f"A soma dos numeros pares é: {somapar}")
print(f"A soma dos numeros impares é: {somaimpar}")

