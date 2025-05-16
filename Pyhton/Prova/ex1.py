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
