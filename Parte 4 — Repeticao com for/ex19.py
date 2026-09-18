# 19. Peça um número e calcule seu fatorial. O fatorial de 5 é 5 × 4 × 3 × 2 × 1 = 120.

print(" --- CALCULADORA DE FATORIAL DO SR EWERTON ---")

numero_fatorial = int(input("Digite seu número para calcular o fatorial: "))

numero_range = numero_fatorial

for ewerton in range(1, numero_range):

    numero_fatorial = numero_fatorial * ewerton
    print(f"x {ewerton} = {numero_fatorial}")

print(f"O fatorial do seu número {numero_range} é: {numero_fatorial}")

#Nota: No meu código, eu fiz a operação inversa do fatorial (fatorial começar com n · (n – 4) · (n – 3) ao invés de n · (n – 1) · (n – 2) ) para ocupar menos linhas de código e para melhor vizualização, entretanto, isso não significa que o resultado sairá errado pois a ordem do produto não altera o resultado.
