nota = int(input("Digite a nota do aluno (0-100): "))

if nota < 60:
    print(f"Nota F (menos de 60)")
elif nota < 70:
    print(f"Nota D (60-69)")
elif nota < 80:
    print(f"Nota C (70-79)")
elif nota < 90:
    print(f"Nota B (80-89)")
elif nota <= 100:
    print(f"Nota A (90-100)")
else:
    print("Nota invalida!!")