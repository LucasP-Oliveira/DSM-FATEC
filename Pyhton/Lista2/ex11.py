idade = int(input("Digite a idade: "))
categoria = input("Digite a categoria(juvenil, adulto, veterano): ").lower()

if idade < 18:
    print(f"menor de idade!! - {idade}")
elif idade < 36:
    print(f"Adulto!! - {idade}")
else:
    print(f"Veterano!!! - {idade}")

if categoria == "juvenil":
    print(f"Jogar do time principal - {categoria}")
elif categoria == "adulto":
    print(f"Jogador do time principal da categoria - {categoria}")
elif categoria == "veterano":
    print(f"Jogar principal da categoria - {categoria}")
else:
    print(f"Categoria invalida !! - {categoria}")