#soma dos pares e a media dos impares

inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
soma_par = 0
soma_impar = 0
cont_impar = 0

for i in range(inicio, fim):
    #print(i)

    if i % 2 == 0:
        print(f"{i} = PAR")
        soma_par += i
    else:
        print(f"{i} = IMPAR")
        soma_impar += i
        cont_impar += 1


print(f"Soma dos pares = {soma_par}")
print(f"Soma dos impares = {soma_impar}")
print(f"Qtds de impares = {cont_impar}")
print(f"A media dos impares = {soma_impar/cont_impar}")