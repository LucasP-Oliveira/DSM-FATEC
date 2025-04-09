#Peça ao usuário três números: início, fim e passo e exiba a sequência correspondente.

inicio = int(input("Digite o numero de inicio: "))
fim = int(input("Digite o numero do fim: "))
passo = int(input("Digite o numero do passo: "))

for i in range(inicio, fim, passo):
    print(i)
