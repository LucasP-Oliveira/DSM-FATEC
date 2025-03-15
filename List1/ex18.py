custoDeFabrica = float(input("Digite o custo da fabrica para produzir um carro: "))

distribuidor = 48 / 100 * custoDeFabrica
impostos = 45 / 100 * custoDeFabrica

preco = custoDeFabrica + distribuidor + impostos

print(f"O preo que o consumidor deve pagar é: {preco}")

