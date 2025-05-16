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
