ativo = True
logado = True
nome = "Ágata"

if ativo and logado:
    print("Bem vindo, usuário(a) ", nome, "!")
elif ativo:
    print("Você precisa estar conectado(a) para entrar!")
else:
    print("Acesso negado!")