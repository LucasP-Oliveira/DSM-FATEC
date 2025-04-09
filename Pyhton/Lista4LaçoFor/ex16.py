#Peça ao usuário um número N e exiba quantos números entre 1 e N são múltiplos de 3 ou 5.

num = int(input("Digite um numero: "))
contador = 0
for i in range(1, num):
    if i % 3 == 0 or i % 5 == 0:
        contador += 1
print(f"Entre 1 e {num}, existem {contador} números que são múltiplos de 3 ou 5.")



