peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

IMC = peso / (altura **2)

if IMC < 18.5:
    print(f"IMC: {IMC:2f} considerado ABAIXO DO PESO!!")
elif IMC < 25:
    print(f"IMC: {IMC:2f} considerado PESO NORMAL!!")
elif IMC < 30:
    print(f"IMC: {IMC:2f} considerado ACIMA DO PESO!!")
else:
    print(f"IMC:{IMC:2f} considerado OBESO!!")