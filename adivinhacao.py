import random

sorteio = random.randint(0, 5)
num = int(input('Escolha um número entre 0 e 5:'))

if num == sorteio:
    print('Parabéns, eu pensei no número', sorteio,'! Você sabe ler mentes!')
else:
    print('Ahhh, não foi dessa vez! Eu pensei no número', sorteio)