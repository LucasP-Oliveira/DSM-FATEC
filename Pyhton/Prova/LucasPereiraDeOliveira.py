#Lucas Pereira de Oliveira - 1051392511043

#1 - Sistema de Hotel – Verificação de Diárias
# Um sistema de hotel deve calcular o valor total da hospedagem. O usuário informa o
# número de diárias. Cada diária custa R$ 120.
# Se o número de diárias for maior que 7, o sistema aplica um desconto de 10% no total.
# Desenvolva esse algoritmo com uso de operadores e estrutura de decisão.

diarias = int(input("Digite o número de diárias: "))

valor_total = diarias * 120
if diarias > 7:
    desconto = valor_total * 0.10
    valor_total -= desconto

print(f"Valor total da hospedagem: R$ {valor_total:.2f}")


#2 - Sistema de Restaurante – Pedido com Adicional
#Um sistema de restaurante oferece dois pratos:
#• Prato A: R$ 20
#• Prato B: R$ 25
#O cliente pode ainda adicionar uma bebida por R$ 5.
#Desenvolva um algoritmo que pergunte qual prato foi escolhido (A ou B), se
#deseja bebida (S ou N) e calcule o valor total do pedido.

prato = input("Escolha o prato (A ou B): ").upper()

if prato == "A":
    valor = 20
elif prato == "B":
    valor = 25
else:
    print("Prato inválido.")
    valor = 0

bebida = input("Deseja bebida? (S ou N): ").upper()

if bebida == 'S':
    valor += 5
if bebida != 'S' and bebida != 'N':
    print("Opção Inválida!")

print(f"Valor total do pedido: R$ {valor:.2f}")

#3 - Pedido de Comida – Soma de Pedidos
#Um sistema de lanchonete recebe o valor de vários pedidos feitos no caixa.
#Os pedidos são feitos em sequência até que o valor 0 seja digitado.
#Calcule e exiba o total da conta usando while.


total = 0

while True:
    valor = float(input("Digite o valor do pedido (Ou 0 para sair): "))

    if valor == 0:
        break

    total += valor

print(f"A soma dos pedidos são: {total:.2f}")

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