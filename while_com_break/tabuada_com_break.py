cont = mult = 0
n = int(input('Digite o valor que você gostaria de ver a tabuada: '))
while n > 0:
    cont += 1
    mult = n * cont
    if cont > 10:
        break
    if n < 0:
        break
    print(n, 'x', cont, '=', mult)
print('Fim da tabuada!')
print('Bons estudos!')