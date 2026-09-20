# 23. Usando a mesma lista, encontre e exiba o maior valor.

lista_ewerton_numeros = [1,69,3,67,76]
maior_numero = lista_ewerton_numeros[0]

for numero in lista_ewerton_numeros:
       if numero > maior_numero:
              maior_numero = numero
print(maior_numero)