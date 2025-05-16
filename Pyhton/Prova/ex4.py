#4 - Sistema de Controle de Quarto – Limite de Pessoas
#Um quarto de hotel suporta até 3 pessoas. Crie um sistema com while que permita
#registrar pessoas até atingir o limite.
#A cada pessoa, exiba: "Pessoa registrada".
#Quando atingir 3, exiba: "Limite atingido"

qtde = 0

while qtde < 3:
    nome = input("Digite o nome para registrar: ")
    qtde += 1
    print(f"Pessoa Registrada: {nome}")

print("Limite Atingido.")

