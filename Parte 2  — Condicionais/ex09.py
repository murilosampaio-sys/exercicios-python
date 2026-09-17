# 9. Peça a média de um estudante e classifique: 6 ou mais é Aprovado; de 4 a 5,9 é Recuperação; abaixo de 4 é Reprovado.

print(" --- APROVAÇÃO DE ALUNOS DO CURSO TÉCNICO DE DS DO SR EWERTON --- ")

nota = float(input("Digite sua nota para a verificação: "))

if (nota >= 6) and (nota <= 10):
    print(f"Sua nota {nota} te aprova de ano!")

elif (nota >= 4) and (nota <= 5.9):
    print(f"Sua nota {nota} te deixa em recuperação.")

elif (nota >= 0) and (nota < 4):
    print(f"Sua nota {nota} te reprova de ano.")

else: 
    print("O valor digitado não é válido.")