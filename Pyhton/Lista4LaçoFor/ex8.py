#Peça 5 notas ao usuário e calcule a média delas.
media = 0

for i in range(1, 6):
    nota = int(input("Digite a nota: "))
    media += nota / 5
print(f"A média das notas dos Alunos {media:.2f}")