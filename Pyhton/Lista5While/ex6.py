#Escreva um programa que continue pedindo ao usuário para inserir notas (0 a 10) e calcule a média dessas notas. O programa deve parar quando o usuário digitar uma nota negativa.
sumNota = 0
qtdeNota = 0

while True:
    nota = int(input("Digite uma nota (0 a 10): "))

    if nota < 0:
        print(f"Iniciando Calculo...")
        print(sumNota)
        print(qtdeNota)
        break
    elif nota > 10:
        print("Nota Inválida!!!")
        continue

    sumNota += nota
    qtdeNota += 1

if qtdeNota > 0:
    media = sumNota / qtdeNota
    print(f"A media das notas é: {media:.2f}")

else:
    print("Nenhuma nota inserida!!")


print("tabela Verdade para perova, numero binário")

