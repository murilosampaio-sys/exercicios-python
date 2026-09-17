# 14. Peça um número e exiba sua tabuada de 1 a 10.

contador = 1
print("--- TABUADA EDUCATIVA COM O TEACHER EWERTON ---")

numero_tabuada = float(input("Digite um número para ver sua tabuada de 1 a 10: "))
while contador < 11:
    print(f"{contador} x {numero_tabuada} = {contador * numero_tabuada :.2f}")
    contador = contador + 1