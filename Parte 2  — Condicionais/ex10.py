# 10. Peça a idade de uma pessoa e informe se ela já pode votar. A idade mínima é 16 anos.

print(" --- SISTEMA DE VALIDAÇÃO DE IDADE EM URNAS --- ")

idade = int(input("Digite sua idade em anos de vida: "))

if idade >= 16:
    print(f"Sua idade de {idade} anos lhe permite votar.")

elif (idade < 16) and (idade >= 2):
    print(f"Sua idade de {idade} anos não lhe permite votar.")

elif (idade < 2) and (idade >= 0):
    print(f"Sua idade de {idade} ano não lhe permite votar.")

else:
    print("Digite um número válido.")