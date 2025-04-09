inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
soma = 0

for i in range(inicio, fim):
    print(i)
    soma += i
print(f"Soma = {soma}")
