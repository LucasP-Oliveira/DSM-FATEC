num = int(input("Digite um número: "))

eh_primo = True

for i in range(2, num):
    if num % i == 0:
        eh_primo = False
        break

if eh_primo and num > 1:
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo.")
