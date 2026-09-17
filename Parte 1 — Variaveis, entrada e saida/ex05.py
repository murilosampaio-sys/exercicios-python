# 5. Peça o preço de um produto e a quantidade comprada. Exiba o valor total, com duas casas decimais.

print("--- SEJA BEM VINDO A LOJA DO MELHOR PROFESSOR DO SESI, EWERTON ---")

preco_produto = float(input("Digite o preço do produto que você quer comprar: "))
quantidade_produto = int(input("Digite a quantidade do produto: "))

preco_final = preco_produto * quantidade_produto

print(f"O preço final do produto que você pegou ficou R$ {preco_final:.2f}.")