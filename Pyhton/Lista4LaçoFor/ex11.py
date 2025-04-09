#Escreva um programa que exiba os números de 1 a 20 e indique se cada um é par ou ímpar.

for i in range(1,21):
    if (i % 2 == 0):
        print(f"{i} é par")
    else:
        print(f"{i} é impar")