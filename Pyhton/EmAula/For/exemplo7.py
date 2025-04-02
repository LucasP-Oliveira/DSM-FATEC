inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))

for i in range(inicio, fim):
    #print(i)

    if i % 2 == 0:
        print(f"{i} = PAR")
    else:
        print(f"{i} = IMPAR")
