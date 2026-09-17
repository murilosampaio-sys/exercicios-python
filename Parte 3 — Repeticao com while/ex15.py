# 15. Peça números ao usuário até que ele digite 0. Ao final, informe quantos números positivos foram digitados.

# Nota: Tomei liberdade para usar listas e o comando len para a resolução do exercício, apesar de estar na pasta de "Parte 3 - Repeticao com while" entretanto isso de forma alguma tira minha autoria do código.

numeros = []
print("Contador de quantidade de números positivos do ewerton")

numero = int(input("Digite qualquer número, caso você digite 0, o programa para de contar e mostra o resultado, caso você digite números negativos, o programa não irá somar o número. : "))

if numero > 0:
    numeros.append(numero)

elif numero < 0:
        print("Número negativo não será adicionado na soma.")

while numero != 0:

    numero = int(input("Digite qualquer número, caso você digite 0, o programa para de contar e mostra o resultado, caso você digite números negativos, o programa não irá somar o número. : "))

    if numero > 0:
        numeros.append(numero)
    elif numero < 0:
        print("Número negativo não será adicionado na soma.")
    else: 
        break

print(f"A quantidade de números positivos adicionados foi de: {len(numeros)}")
