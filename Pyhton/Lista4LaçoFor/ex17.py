num = int(input("Digite um numero: "))

for i in range(num, 0, -1):
    if i % 2 == 0:
        par = num / 2
        print(f"resultado: {par}")
        break
    else:
        impar = num * 3
        print(f"resultado: {impar}")
        break
