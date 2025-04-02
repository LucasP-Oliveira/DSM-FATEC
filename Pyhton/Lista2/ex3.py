idade = int(input("Digite a sua idade: "))

if idade < 13:
    print("Criança (0-12)")
elif idade < 18:
    print("Adolescente (13-17)")
elif idade < 65:
    print("Adulto (18-64)")
else:
    print("Idoso (65+)")