from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor entre 0 e 10: '))
    cpu = randint(0,10)
    total = jogador + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar?')).strip().upper()
    print('Você jogou ',jogador, 'e a máquina jogou ', cpu, '. O total foi de ', total)
    if tipo == 'P':
        if total % 2 == 0:
            print('Muito bem, ponto para você!')
            v += 1
        else:
            print('Que pena, ponto para seu oponente!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Muito bem, ponto para você!')
            v += 1
        else:
            print('Que pena, ponto para seu oponente!')
            break
    print('Vamos jogar novamente!')
print('Fim de jogo! Você teve ',v, 'vitórias!')