idade = int(input("Digite a sua idade: "))

if idade < 18:
    print(f"com essa idade: {idade} voce é de menor!!")
elif idade < 65:
    print(f"Com essa idade: {idade} vocé é adulto!!")
else:
    print(f"com essa idade: {idade} voce é idoso!!")
