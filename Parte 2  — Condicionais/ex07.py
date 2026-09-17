# 7. Peça dois números e exiba qual é o maior. Se forem iguais, informe isso.

print("--- Calculadora de comparação de números do Ewertonzinhofofo ---")

numero1 = int(input("Digite seu primeiro número: "))
numero2 = int(input("Digite seu segundo número: "))

if numero1 > numero2:
    print(f"O primeiro número: {numero1} é maior que o segundo número: {numero2}.")

elif numero2 > numero1:
    print(f"O segundo número: {numero2} é maior que o primeiro número: {numero1}.")

else:
    print("Os dois números são iguais!")

