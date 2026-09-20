25. # Dada a lista [3, 7, 1, 9, 4], exiba os itens na ordem inversa.
lista_fofaewerton = [3, 7, 1, 9, 4]
contador = 1
quantidade = len(lista_fofaewerton)

for i in range(quantidade):
    print(lista_fofaewerton[quantidade - contador])
    contador = contador + 1