# 6. Peça um número e informe se ele é par ou ímpar.

print("--- Calculadora de número par ou ímpar do Ewertonzinho ---")

numero = int(input("Digite seu número: "))

if numero % 2 == 0:
    print(f" O número {numero} é par.")
else:
    print(f" O número {numero} é ímpar.")