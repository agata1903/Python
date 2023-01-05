num = int(input('Digite um número: '))
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[34m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(i, end=' ')
