kmPercorrido =  float(input("Digite a quantidade de KM rodado: "))
diasAlugado = int(input(("Digite a quantidade de dias com o carro: ")))

valordiarioCarro = 90.00
valorKmRodado = 0.20

preçodiario = diasAlugado * valordiarioCarro
preçoKM = kmPercorrido * valorKmRodado

print(f"O preço total a pagar é: {preçoKM + preçodiario}")