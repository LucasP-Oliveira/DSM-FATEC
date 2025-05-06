import random

num_secret = random.randint(1, 10)
i = 3

for i in range(1, i + 1):
    num = int(input("Digite um numero: "))

    if num == num_secret:
        print("Você Acertou o numero!!")
        break

    elif num < num_secret:
        print("O numero é maior")

    else:
        print("O numero é menor")
print("Acabou as tentativas")