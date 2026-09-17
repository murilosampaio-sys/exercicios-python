# 12. Peça números ao usuário e vá somando. Quando ele digitar 0, pare e exiba a soma.
#Eewerton

print("--- SOMATÓRIO DE NÚMEROS - DIGITE 0 PARA SAIR OU UMM NÚMERO PARA SOMAR ---")

soma = 0
numero = float(input("Digite um número para somar ou 0 para encerrar: "))

while numero != 0:
    soma = soma + numero
    numero = float(input("Digite outro número para somar ou 0 para encerrar: "))

print(f"O total dos seus números somados foi de: {soma}")

