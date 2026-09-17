# 13. Peça uma senha ao usuário e continue pedindo até que ele digite senai123. Ao acertar, exiba "Acesso liberado".

senha = 'senai123'

print("--- BEM VINDO AO SISTEMA DO SESI SENAI PROFESSOR EWERTON ---")

tentativa_senha = input("Digite sua senha para entrar no seu email: ")

while tentativa_senha != senha:
    print("Senha incorreta! Tente novamente.")
    tentativa_senha = input("Digite sua senha para entrar no seu email: ")

print("Acesso liberado aos serviços da Escola SESI SENAI.")