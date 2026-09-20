# 24. Dada a lista [5, 12, 8, 20, 3, 15], informe quantos itens são maiores que 10.
lista_uwu = [5, 12, 8, 20, 3, 15]
quantidade_maiores = 0

for numero in lista_uwu:
    if numero > 10:
        print(f"{numero} é maior que 10.")
        quantidade_maiores = quantidade_maiores + 1

print(f"A quantidade de itens maiores que 10 é: {quantidade_maiores}")