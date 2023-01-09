n = int(input('Digite um número: '))
soma = 0
cont = 0
while n != 999:
    print(n)
    n +=1
    cont = cont + 1
    soma = soma + n
    n = int(input('Digite um número: '))
print('A soma entre os ',cont, 'valores foi de ', soma)