n = s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print('A soma de todos os ',c, ' números foi de ',s)
