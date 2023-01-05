maior = 0
menor = 0
for i in range(1,8):
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Existem ', maior, 'pessoas maiores de 18 anos e ', menor, 'pessoas menores de 18 anos.')

